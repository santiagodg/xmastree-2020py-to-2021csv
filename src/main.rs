use std::env;
use std::fs::{File, OpenOptions};
use std::io::{Read, Write};
use std::process::Command;

fn main() {
    let arguments: Vec<String> = env::args().collect();

    if arguments.len() < 2 {
        panic!("Not enough arguments");
    }

    let py_script = &arguments[1];
    let frame_amount: i32 = arguments[2].parse().unwrap();

    let mut file = File::open(py_script).unwrap();

    let mut file_contents = String::new();

    file.read_to_string(&mut file_contents).unwrap();

    file_contents = file_contents.replace("\t", "    ");

    let new_contents = file_contents
        .lines()
        .filter(|&line| {
            if line == "    import board" {
                false
            } else if line == "    import neopixel" {
                false
            } else {
                true
            }
        })
        .fold(
            String::from("import xmastree_2020py_to_2021csv\n"),
            |mut acc, line| {
                if line
                    == "    pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)"
                {
                    acc.push_str("    pixels = xmastree_2020py_to_2021csv.Pixels(PIXEL_COUNT)\n");
                    return acc;
                } else if line == "    while run == 1:" {
                    acc.push_str(&format!("    while run <= {}:\n", frame_amount));
                    acc.push_str("        run += 1\n");
                    return acc;
                } else if line == "    while True:" {
                    acc.push_str("    frameCounter2021 = 0\n");
                    acc.push_str(&format!("    while frameCounter2021 < {}:\n", frame_amount));
                    acc.push_str("        frameCounter2021 += 1\n");
                    return acc;
                } else if line.contains("Python/coords.txt") {
                    acc.push_str(&line.replace("Python/coords.txt", "coords_2021.txt"));
                    return acc;
                }

                acc.push_str(line);
                acc.push_str("\n");
                acc
            },
        );

    let mut file = OpenOptions::new()
        .write(true)
        .truncate(true)
        .create(true)
        .open(&py_script.replace(".py", &format!(".{}frames.py", frame_amount)))
        .unwrap();

    file.write(new_contents.as_bytes()).unwrap();

    Command::new("cmd")
        .args([
            "/C",
            "py",
            &py_script.replace(".py", &format!(".{}frames.py", frame_amount)),
            ">",
            &py_script.replace(".py", ".csv"),
        ])
        .status()
        .unwrap();
}
