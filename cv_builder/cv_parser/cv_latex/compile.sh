echo "cd "$(pwd)"/cv_latex\n"
cd $(pwd)"/cv_parser/cv_latex"
echo "cd "$(pwd)"/cv_latex\n"
cp ".."$1 "./image.jpg"
pdflatex template_auto.tex 
rm template_auto.out
rm template_auto.log
rm template_auto.aux
mv template_auto.pdf "../static/cv_parser/"$2
rm "image.jpg"