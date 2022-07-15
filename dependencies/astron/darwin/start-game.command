cd "$(dirname "$0")"
cd ../..
cd ..
export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
export DYLD_FRAMEWORK_PATH="Frameworks"

# Get the user input:
read -p "Username: " ttgUsername
read -p "Gameserver (DEFAULT:  localhost): " TTG_GAMESERVER
TTG_GAMESERVER=${TTG_GAMESERVER:-"localhost"}

# Export the environment variables:
export ttgUsername=$ttgUsername
export ttgPassword="password"
export TTG_PLAYCOOKIE=$ttgUsername
export TTG_GAMESERVER=$TTE_GAMESERVER

echo "==============================="
echo "Starting Disney's Toontown Online..."
echo "Username: $ttgUsername"
echo "Gameserver: $TTG_GAMESERVER"
echo "==============================="

python3.9 -m toontown.toonbase.ToontownStart
