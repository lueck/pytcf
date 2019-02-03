Tools for reading files in Text Corpus Format (TCF)
===================================================

[TCF](https://weblicht.sfs.uni-tuebingen.de/weblichtwiki/index.php/The_TCF_Format)
is an interchange format for linguistic annotations. It is used by the
[WebLicht](https://weblicht.sfs.uni-tuebingen.de/) webservices.

This python package offers some lightwight command line tools for
reading TCF files. If you want to write webservices, that integrate
into WebLicht, please have a look at
[TCFlib](https://github.com/SeNeReKo/TCFlib/tree/master/tcflib). If
your favourite programming language is Haskell, please have a look at
my [htcf](https://github.com/lueck/htcf), but this package's `tcf2csv`
runs magnitudes faster.


## Requirements ##

The tools are written in the Python programming language. So
[Python](https://www.python.org/downloads/), version 2.7, is required
to use it.


## Installation ##

Clone this repositoy, open a terminal and `cd` into the root directory
of the clone. Then run

```shell
$ pip install -e .
```


## Usage ##

After installation run `tcf2csv -h` on a terminal in order to read
a usage note.

## License ##

[GPL V3](http://www.gnu.org/licenses/gpl-3.0.txt)
