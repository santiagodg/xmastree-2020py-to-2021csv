# xmastree-2020py-to-2021csv

Turn [standupmaths/xmastree2000](https://github.com/standupmaths/xmastree2020) animation scripts
into 2021 CSV animation files.

This is a primarily a Rust project. I'm not actually using any special Rust features. I'm learning the language and figured I could try make a quick command for this.

This project depends on having a Python3 `py` command in the running environment.

## Usage

The tool takes a two arguments: 
* `file`: a python script filename containing 2020's animation,
* `frames_amount`: the amount of frames to output. This is required since scripted animations don't end, so we have to cut them at some point.

```
cargo run <file> <frames_amount>
```

## Example

Run the following command:

```
cargo run xmaslights-spin.py 500
```

This generates two new files: 
* `xmaslights-spin.500frames.py`: New script that will print pixel colors 
instead of sending them to a microcontroller.
* `xmaslisghts-spin.csv`: The output CSV animation file.

## Other tools

### 2021_coords_to_2020.py

The script `2021_coords_to_2020.py` turns 2021's coordinates in GIFT format into the format used to
specify 2020 coordinates and prints it out.

#### Example

Run the command (using Windows):

```
py 2021_coords_to_2020.py > coords_2021.txt
```

It takes `matts_coords_2021.csv` file in GIFT format and prints the 2020 coordinates format, which is
then saved to the `coords_2021.txt` file. The `coords_2021.txt` is used by the Rust tool to calculate
the animation based on 2021's coordinates.

### old_coords_range.py

The script `old_coords_range.py` reads the `coords.txt` file and prints out the minimum and maximum value
for each of the coordinate dimensions. These values were then used to generate the `coords_2021.txt` file
with its values scaled to 2020's dimension range so that old animations work as expected.

```
py old_coords_range.py
```

## Credits

The `xmaslights-spin.py` animation was taken from [standupmaths/xmastree2020](https://github.com/standupmaths/xmastree2020)'s repository.

The `matts_coords_2021.csv` coordinates file was taken from [standupmaths/xmastree2021](https://github.com/standupmaths/xmastree2021)'s repository, file `coords_2021.csv`.
