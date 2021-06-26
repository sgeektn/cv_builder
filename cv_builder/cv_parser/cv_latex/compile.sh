cd $(pwd)"/cv_parser/cv_latex"
echo "photo"
echo $1
cp ".."$1 $(pwd)"/image.jpg"
echo "cp .."$1 $(pwd)"/image.jpg zeb"
pdflatex --no-shell-escape template_auto.tex 
rm template_auto.log
rm template_auto.aux
rm template_auto.run.xml
rm template_auto.bcf
rm page1sidebar.aux
mv template_auto.pdf "../static/cv_parser/"$2
rm "image.jpg"