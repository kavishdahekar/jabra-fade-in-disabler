build-release:
	rm -rf ./build
	rm -rf ./dist 
	pyinstaller --noconfirm --clean \
	--noconsole \
	--onefile \
	--name 'Jabra FadeIn Disabler' \
	--icon=jabra-fade-in-disabler/assets/ClippingSound.icns \
	--add-data 'jabra-fade-in-disabler/assets/*:assets' \
	jabra-fade-in-disabler/main.py

build-dmg:
	rm ./dist/*.dmg || true
	create-dmg \
	--volname "Jabra FadeIn Disabler" \
	--volicon "jabra-fade-in-disabler/assets/ClippingSound.icns" \
	--window-pos 200 120 \
	--window-size 600 500 \
	--icon-size 100 \
	--icon "Jabra FadeIn Disabler.app" 175 180 \
	--hide-extension "Jabra FadeIn Disabler.app" \
	--app-drop-link 425 180 \
	"dist/Jabra FadeIn Disabler.dmg" \
	"dist/"

build-debug:
	pyinstaller --noconfirm --clean \
	--onefile \
	--name 'jabra-fade-in-disabler-debug' \
	--icon=jabra-fade-in-disabler/assets/ClippingSound.icns \
	--add-data 'jabra-fade-in-disabler/assets/*:assets' \
	jabra-fade-in-disabler/main.py