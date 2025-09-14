export TEXINPUTS=".:styFiles:"

declare -a arr=("AquilaIOrbit" "Astrome" "CandDataStructures" "DataScienceBootcampUdemy" "DigitalDesign" "Extended_CV" "FPGAPrimer" "HLS" "Interview" "Job" "Maitreya_CV" "MotivationLetter" "P2FSemi" "Python" "QraqonReport" "QuickReviseVLSI" "Verilog" "Zynq")   # add your folder name here.

declare -a XeArr=("CoverLetter")   # add your folder name here.


for DIR in "${XeArr[@]}"
do
   cd $DIR
   xelatex $DIR.tex | grep -i "warning\|error"    #comment grep for further debugging
#    rm -rf main.out main.log  main.aux main.toc
   mv $DIR.pdf ../build/
   cd ..
done
   
for DIR in "${arr[@]}"
do
   cd $DIR
   pdflatex $DIR.tex | grep -i "warning\|error"    #comment grep for further debugging
#    rm -rf main.out main.log  main.aux main.toc
   mv $DIR.pdf ../build/
   cd ..
done

printf "\n\nCompilation Done.\nCheck warnings/errors.\nFresh Pdfs are ready.\nFor further debugging check build.sh\n\n"
