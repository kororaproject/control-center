# Makefile for source rpm: control-center
# $Id$
NAME := control-center
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
