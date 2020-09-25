cat query.sql | xargs -I{} mysql -h 127.0.0.1 -u injection_test -pP@ssw0rd injection_test -e "{}"
