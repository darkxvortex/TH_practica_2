FROM --platform=linux/arm64 ubuntu:22.04

RUN apt update && apt full-upgrade -y && apt install xinetd build-essential -y && apt install libseccomp-dev -y

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./entrypoint.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./pwnthemall2 /chall
RUN chmod +x /chall

COPY ./flag.txt /tmp/flag.txt

CMD ["/start.sh"]
