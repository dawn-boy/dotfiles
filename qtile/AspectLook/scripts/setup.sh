set -e

# yay -S polybar

init(){
		echo "[Info] Making changes at $HOME path"
		echo "[Ask] Wish to proceed? (yes/no): "

		choice=""
		read choice

		echo "----- BEGIN EXECUTION -----" >> log
		echo "[var] choice: $choice " >> log

		if [ "$choice" != "yes" ];
		then
				exit 1;
		fi

		mkdir $HOME/.ithub
		mkdir $HOME/.ithub/dotfiles
		git clone https://github.com/dawn-boy/dotfiles.git $HOME/.ithub/dotfiles
}


echo "Initialising... Please wait."
#init 
mkdir $HOME/config
path=
for link in $(ls ../config/);
do
		ln -s ~/.ithub/dotfiles/qtile/AspectLook/config/$link $HOME/config/
done

