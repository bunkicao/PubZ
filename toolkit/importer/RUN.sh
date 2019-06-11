#URL="https://pubz.private/api/rest/"
URL_BASE="http://localhost:8080/api/rest"
USER="test@test.com"


mode=$1

if [ ${mode} == "auth" ];
then
    URL="${URL_BASE}/api-token-auth/"
    python auth_token.py --url ${URL} -u ${USER}
elif [ ${mode} == "author" ]; then
    CSV="./csv/PubZ_Authors.csv"
    python3 authors.py CSV \
	   --url-base ${URL_BASE} \
	   -u ${USER} \
	   -f ${CSV}
elif [ ${mode} == "book" ]; then
    CSV="./csv/PubZ_Books.csv"
    python3 book.py CSV \
	   --url-base ${URL_BASE} \
	   -u ${USER} \
	   -f ${CSV} 
fi
