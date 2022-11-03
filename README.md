# Gram-Schmidt Calculator
A calculator for computing orthogonal and orthonormal bases in R^n. [Wikepidia description of this process.](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process)


### Known Issues
* I've implemented a commonly used formatter that helps with the floating point issue when converting from decimal to fraction form. Although, this doesn't work reliably. If the answers you're receiving are ridiculously incorrect, comment out that line. I've labeled it inside the code. 

### Notes
* By default the vectors are in R^3 (3-vectors). You may enter the vectors in the larger matrix (labeled as A), or as individual vectors if you'd prefer. There is already a built in algorithm to break up the columns, so it is likely easy to enter it as a nx3 matrix.
* This expands upon the numpy linalg library -- requires the pip installation of numpy.py

### Goals
* Build a more robust library out of this

Please email me at ephraimjzimmerman@gmail.com if you have any recommendations or comments. 
