# Run this command to generate documents
# "& C:/Python/Python310/python.exe .\build.py"

import os

repo_path = os.path.dirname(os.path.realpath(__file__))


dir_list = os.listdir() 
# print(dir_list)
exclude_list = [".git", ".gitignore", ".vscode", 'build', "build.py", 'build.sh', 'CoverLetter', 'format.tex', 'README.md', "styFiles"]

tex_dir_list = []
for dir in dir_list:
   # Exclude following from compiling
   if(exclude_list.count(dir) != 1):
      tex_dir_list.append(dir)    #List of latex document directories after excluding  print(tex_dir_list) 

tex_files = []
build_files = []
for tex_dir in tex_dir_list:
   tex_files.append(os.path.join(repo_path, tex_dir, tex_dir + "." + "tex"))
   build_files.append(os.path.join(repo_path, "build", tex_dir + "." + "pdf"))

# Remove all generated files in build folder
out_dir = (os.path.join(repo_path, 'build'))
for f in os.listdir(out_dir):
    os.remove(os.path.join(out_dir, f))

# latex compilation
for doc in tex_files:
   os.path.basename(doc)
   base=os.path.basename(doc)   
   os.chdir(os.path.join(repo_path, os.path.splitext(base)[0]))
   # print(os.getcwd())
   command_string = ("latexmk -pdf -pdflatex=" + "pdflatex --max-print-line=10000 -quiet -synctex=1 -recorder -file-line-error  -interaction=nonstopmode -output-directory=" + '"{}"'.format(out_dir) + ' {}'.format(doc) )
   os.system(command_string)

#  any single document for testing by changing the sample_doc variable with the document name
# sample_doc = "Astrome"
# os.chdir(os.path.join(repo_path, sample_doc))

# doc = (os.path.join(repo_path, sample_doc, sample_doc + "." + "tex"))
# command_string = ("latexmk -pdf -pdflatex=" + "pdflatex --max-print-line=10000 -quiet -synctex=1 -recorder -file-line-error  -interaction=nonstopmode -output-directory=" + '"{}"'.format(out_dir) + ' {}'.format(doc) )
# os.system(command_string)

# for build in build_files:
#    if(os.path.isfile(build) == 1):
#       print(build, "is generated")

for build in build_files:
   if(os.path.isfile(build) == 0):
      print(build, "is not generated")





# Generate any single document for testing by changing the sample_doc variable with the document name
# sample_doc = "QraqonReport"
# doc = (os.path.join(repo_path, sample_doc, sample_doc + "." + "tex"))
# command_string = ("latexmk -pdf -pdflatex=" + "pdflatex --max-print-line=10000 -quiet -synctex=1 -recorder -file-line-error  -interaction=nonstopmode -output-directory=" + '"{}"'.format(out_dir) + ' {}'.format(doc) )
# os.system(command_string)
















# command = ['pdflatex', '-interaction=nonstopmode', '--max-print-line=10000', '-synctex=1', '-file-line-error', '-recorder', '-output-directory', out_dir, python_latex]
# command_list = [command, command, command]
# subprocess.call(['command', 'command'])

# command_string = ("pdflatex --max-print-line=10000 -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory=" + '"{}"'.format(out_dir) +" "+'"{}"'.format(python_latex))
# print(command_string)
# os.system("%.format(command_string,command_string))



# command_string = ("pdflatex --max-print-line=10000 -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory=" + '"{}"'.format(out_dir) +" "+'"{}"'.format(python_latex) + " & "+
# "pdflatex --max-print-line=10000 -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory=" + '"{}"'.format(out_dir) +" "+'"{}"'.format(python_latex) + " & "+
# "pdflatex --max-print-line=10000 -synctex=1 -interaction=nonstopmode -file-line-error -recorder -output-directory=" + '"{}"'.format(out_dir) +" "+'"{}"'.format(python_latex))




# print(command_string)
# subprocess.Popen(command_string)

# subprocess.getoutput(['pdflatex', '-interaction=nonstopmode', '--max-print-line=10000', '-synctex=1', '-file-line-error', '-recorder', '-output-directory', out_dir, python_latex])