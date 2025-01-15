user=$1

mkdir /home/$user/.ithub
mkdir /home/$user/.ithub/dotfiles
git clone https://github.com/dawn-boy/dotfiles.git /home/$user/.ithub/dotfiles

ln -s /home/$user/.ithub/dotfiles/qtile/2.\ AspectLook/polybar /home/$user/.config/.

