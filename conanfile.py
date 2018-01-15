#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class JC_VoronoiConan(ConanFile):
    name = "jc_voronoi"
    version = "0.3.0"
    url = "https://github.com/bincrafters/conan-jc_voronoi"
    description = "A C implementation for creating 2D voronoi diagrams"
    
    # Indicates License type of the packaged library
    license = "MIT"
    
    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]
    
    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    
    def source(self):
        source_url = "https://github.com/JCash/voronoi"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "voronoi-" + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)


    def package(self):
        include_folder = os.path.join(self.source_subfolder, "src")
        self.copy(pattern="LICENSE")
        self.copy(pattern="jc_voronoi.h", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
