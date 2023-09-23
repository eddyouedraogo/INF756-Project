#!/bin/bash
echo "Getting current directory" 
current_dir=$(dirname "$(realpath $0)")
echo "${current_dir}"

echo "Accessing servers directory"
intelligence_dir="${current_dir}/intelligence"
objetcs_dir="${current_dir}/objects"
simulation_dir="${current_dir}/simulation"

echo "Accessing intelligence" 
cd "${intelligence_dir}"

echo "Starting intelligence server"
python "${intelligence_dir}"/manage.py runserver 8000

