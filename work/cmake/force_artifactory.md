# Forcing Cmake To Download From Artifactory

You can force the local build to download artifacts (instead of building them)
by adding 
    SET(CORE_LIBS_PATH "")
to the top of your CMakeLists.txt file.
