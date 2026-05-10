#!/usr/bin/env bash
#
# Run jekyll serve and then launch the site

prod=false
drafts=false
future=false
command="bundle exec jekyll s -l"
host="127.0.0.1"
port="4000"

help() {
  echo "Usage:"
  echo
  echo "   bash /path/to/run [options]"
  echo
  echo "Options:"
  echo "     -H, --host [HOST]    Host to bind to."
  echo "     -P, --port [PORT]    Port to bind to."
  echo "     -d, --drafts         Include posts from _drafts for local preview."
  echo "     -f, --future         Include posts with future dates."
  echo "     -p, --production     Run Jekyll in 'production' mode."
  echo "     -h, --help           Print this help information."
}

while (($#)); do
  opt="$1"
  case $opt in
  -H | --host)
    host="$2"
    shift 2
    ;;
  -P | --port)
    port="$2"
    shift 2
    ;;
  -d | --drafts)
    drafts=true
    shift
    ;;
  -f | --future)
    future=true
    shift
    ;;
  -p | --production)
    prod=true
    shift
    ;;
  -h | --help)
    help
    exit 0
    ;;
  *)
    echo -e "> Unknown option: '$opt'\n"
    help
    exit 1
    ;;
  esac
done

command="$command -H $host -P $port"

if [ -d /opt/homebrew/opt/ruby@3.3/bin ]; then
  export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
fi

if $drafts; then
  command="$command --drafts"
fi

if $future; then
  command="$command --future"
fi

if $prod; then
  command="JEKYLL_ENV=production $command"
fi

if [ -e /proc/1/cgroup ] && grep -q docker /proc/1/cgroup; then
  command="$command --force_polling"
fi

echo -e "\n> $command\n"
eval "$command"
