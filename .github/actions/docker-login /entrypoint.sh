# .github/actions/test-my-name/entrypoint.sh
#!/bin/sh

echo "::set-output name=greeting::Hello, $1!"
