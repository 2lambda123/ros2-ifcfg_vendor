cmake_minimum_required(VERSION 3.5)

project(ifcfg_vendor)

find_package(ament_cmake REQUIRED)
find_package(PythonInterp 3 REQUIRED)

include(ExternalProject)
  ExternalProject_Add(ifcfg-4d846c7
    URL https://github.com/ftao/python-ifcfg/archive/releases/0.18.zip
    URL_MD5 1325b4fb0a2b85d6539bd4cfca993c7f
    TIMEOUT 60
    BUILD_IN_SOURCE 1
    CONFIGURE_COMMAND ""
    INSTALL_COMMAND ""
    BUILD_COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/set_env.py ${CMAKE_CURRENT_BINARY_DIR}/ifcfg_install
  )

install(
    DIRECTORY
      ${CMAKE_CURRENT_BINARY_DIR}/ifcfg_install/
    DESTINATION
      ${CMAKE_INSTALL_PREFIX}
)

ament_package()
