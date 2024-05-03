# script for initializing a new project with this preset
# flags:
# -p project_name to be set in CMakeLists.txt, readme.md and Doxyfile
# -d description to be set in CMakeLists.txt, readme.md and Doxyfile
while getopts p:d: flag
do
  case "${flag}" in
    p) project_name=${OPTARG};;
    d) description=${OPTARG};;
  esac
done

echo "project name: $project_name";
echo "description : $description";

sed -i "s/<project_name>/$project_name/g" CMakeLists.txt readme.md
sed -i "s/<project_description>/$project_description/g" CMakeLists.txt readme.md