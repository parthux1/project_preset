files=$(ls | grep .gv)

out_dir="pngs"

# create output-folder if nonexistent
if ! test -d $out_dir; then
	mkdir "$out_dir"
	echo "created dir $out_dir"
fi

echo "Try to render all present .gv files piped trough c preprocessor"

for file in $files; do
	# filename w/o extension will be used for output file
	filename="${file%%.*}"
	
	echo building $file

	# generate picture
	# we resolve macros for style generation using the c preprocessor
	cpp $file | dot -Tpng > "$out_dir/$filename.png"

	echo done
done
