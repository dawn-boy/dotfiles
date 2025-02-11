# yay -S polybar

init(){
		echo "[Info] Making changes at $HOME path"
		echo "[Ask] Wish to proceed? (yes/no): "

		choice=""
		read choice

		echo "----- BEGIN EXECUTION -----"
		echo "[var] choice: $choice " 

		if [ "$choice" != "yes" ];
		then
				exit 1;
		fi
}


echo "Initialising... Please wait."
init 
for link in $(ls ../config/);
do
		ln -s ~/.github/dotfiles/qtile/AspectLook/config/$link $HOME/.config/
done

echo "Setting up walls"
ln -s ~/.github/walls ~/Pictures/. 

