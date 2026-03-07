# Read from the file file.txt and print its transposed content to stdout.
awk '{
  for (i = 1; i <= NF; i++) {
    col[i] = col[i] (NR > 1 ? " " : "") $i
  }
}
END {
  for (i = 1; i <= NF; i++) {
    print col[i]
  }
}' file.txt