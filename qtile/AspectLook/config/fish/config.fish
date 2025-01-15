if status is-interactive
    # Commands to run in interactive sessions can go here
        clear
	fortune /home/Dew/.github/cookies/cookies
	starship init fish | source
	cat ~/.cache/wal/sequences &
	set fish_greeting
	set -U fish_user_paths ~/.github/cmds/ $fish_user_paths
end

