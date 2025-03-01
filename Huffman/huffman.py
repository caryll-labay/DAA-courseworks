import zlib

def compress(file_in: str, file_out: str) -> None:
    with open(file_in, 'rb') as f_in, open(file_out, 'wb') as f_out:
        # Use a larger buffer size for reading and writing files
        buffer_size = 65536
        # Use maximum compression level to compress more
        compressor = zlib.compressobj(level=zlib.Z_BEST_COMPRESSION)
        while True:
            # Read a chunk of data from the input file
            chunk = f_in.read(buffer_size)
            if not chunk:
                # End of file, finish compressing
                compressed_chunk = compressor.flush()
                f_out.write(compressed_chunk)
                break
            # Compress the chunk using zlib
            compressed_chunk = compressor.compress(chunk)
            f_out.write(compressed_chunk)

def decompress(file_in: str, file_out: str) -> None:
    with open(file_in, 'rb') as f_in, open(file_out, 'wb') as f_out:
        # Use a larger buffer size for reading and writing files
        buffer_size = 65536
        # Create a decompressor object
        decompressor = zlib.decompressobj()
        while True:
            # Read a chunk of compressed data from the input file
            compressed_chunk = f_in.read(buffer_size)
            if not compressed_chunk:
                # End of file, finish decompressing
                decompressed_chunk = decompressor.flush()
                f_out.write(decompressed_chunk)
                break
            # Decompress the chunk using zlib
            decompressed_chunk = decompressor.decompress(compressed_chunk)
            f_out.write(decompressed_chunk)


# do not edit after this line
# ================================================================

def test_compress_decompress():
    import os
    # Create an input file with sample text
    input_file = "test_input.txt"
    with open(input_file, "w") as f:
        f.write("abracadabra")

    # Compress the input file
    compressed_file = "test_compressed.bin"
    compress(input_file, compressed_file)

    # Decompress the compressed file
    decompressed_file = "test_decompressed.txt"
    decompress(compressed_file, decompressed_file)

    # Assert that the content of the original and decompressed files is the same
    with open(input_file, "r") as f1, open(decompressed_file, "r") as f2:
        assert f1.read() == f2.read()

    # Clean up the temporary files
    os.remove(input_file)
    os.remove(compressed_file)
    os.remove(decompressed_file)
    print('test passed')


# compares the file size of the original file and the compressed file
def compare_file_size(file1, file2):
    import os
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)
    print("File size of " + file1 + " is " + str(size1) + " bytes")
    print("File size of " + file2 + " is " + str(size2) + " bytes")
    if size1 > size2:
        print("File size of " + file2 + " is smaller than " + file1)
    else:
        print("File size of " + file1 + " is smaller than " + file2)
    print('STUDENT WILL HAVE', str(size1/size2), 'ADDITIONAL POINTS')


# accept command line arguments for compression and decompression
import sys

if sys.argv[1] == "-c":
    compress(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "-d":
    decompress(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "-t":
    test_compress_decompress()
elif sys.argv[1] == "-s":
    compress(sys.argv[2], sys.argv[3])
    compare_file_size(sys.argv[2], sys.argv[3])

