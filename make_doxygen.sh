# generate pngs
cd doc/diagrams
sh render_all.sh

# autolink markdown files according to doc/autoref.json

# register all markdown files
# move to doc/
cd ..

files_md=`ls markdown/*.md`

echo "calling autoref for following fields:\n${files_md}"

# append all doc files here
python3 autoref.py -f ${files_md}

# generate doc
# move to project-main
cd ..

doxygen

# remove autoref-folder
rm doc/autoref_out -r
