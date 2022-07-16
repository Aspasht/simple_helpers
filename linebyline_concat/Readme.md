# LineByLine Concatenate
  ## This script take all the line from a file and concat to all the lines of other file.
  
# Usage
    ./linebylineconcat.sh file1.txt file2.txt
    
# Example  
     cat file1.txt
        https://example.com/
        http://example.com/
        
     cat file2.txt
        id=1
        id=admin&role=admin
# Result
    https://example.com/?id=1=XSS
    http://example.com/?id=1=XSS
    https://example.com/?id=admin&role=admin=XSS
    http://example.com/?id=admin&role=admin=XSS
    
