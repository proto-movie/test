# MUBI Browse (Android)

A fullscreen WebView wrapper around the browse prototype on GitHub Pages:
https://proto-movie.github.io/test/ClaudeiOS/browse_prototype1.html

It loads the live page, so pushing prototype changes updates the app without a rebuild.

**Install:** open https://proto-movie.github.io/test/ClaudeAndroid/MUBI-Browse.apk on the phone
and allow installing from the browser when Android asks.

**Rebuild** (needs Java 17 and the Android SDK):

```sh
export JAVA_HOME=/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home
./gradlew assembleDebug
cp app/build/outputs/apk/debug/app-debug.apk MUBI-Browse.apk
```

The start URL lives in `app/src/main/res/values/strings.xml`.
