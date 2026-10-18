target_commit="f67cb68e0e6f080c908c2dbeaa4e4a94ba45e663"

IFS=$'\n'; a=$(git log | grep -E "^commit (.+)$" | sed -r "s/commit (.+)/\1/"); for i in $a; do if [ "$i" = "$target_commit" ]; then break; fi; git revert $i; echo reverted $i; done
