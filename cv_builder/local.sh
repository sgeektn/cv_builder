curl http://localhost:8000/
curl http://localhost:8000/FR
curl http://localhost:8000/EN
httrack http://127.0.0.1:8000/  -O "localversion/cv"  -%v 
cv_fr=$(find localversion/cv/127.0.0.1_8000 -name "*_fr.html")
rm -rf $cv_fr
cv_fr=$(basename "$cv_fr")
cv_fr_pdf="${cv_fr%.*}"

cv_en=$(find localversion/cv/127.0.0.1_8000 -name "*_en.html")
rm -rf $cv_en
cv_en=$(basename "$cv_en")
cv_en_pdf="${cv_en%.*}"

vi localversion/cv/127.0.0.1_8000/index.html -c "%s/$cv_fr/static\/cv_parser\/$cv_fr_pdf\.pdf/g" -c "wq"
vi localversion/cv/127.0.0.1_8000/FR.html -c "%s/$cv_fr/static\/cv_parser\/$cv_fr_pdf\.pdf/g" -c "wq"
vi localversion/cv/127.0.0.1_8000/EN.html -c "%s/$cv_fr/static\/cv_parser\/$cv_fr_pdf\.pdf/g" -c "wq"

vi localversion/cv/127.0.0.1_8000/index.html -c "%s/$cv_en/static\/cv_parser\/$cv_en_pdf\.pdf/g" -c "wq"
vi localversion/cv/127.0.0.1_8000/FR.html -c "%s/$cv_en/static\/cv_parser\/$cv_en_pdf\.pdf/g" -c "wq"
vi localversion/cv/127.0.0.1_8000/EN.html -c "%s/$cv_en/static\/cv_parser\/$cv_en_pdf\.pdf/g" -c "wq"

mv localversion/cv/127.0.0.1_8000 .
tar -czvf localversion.tar.gz 127.0.0.1_8000
rm -rf localversion
rm -rf 127.0.0.1_8000