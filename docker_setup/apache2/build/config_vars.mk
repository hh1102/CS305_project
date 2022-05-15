exp_exec_prefix = /usr/local/apache2
exp_bindir = /usr/local/apache2/bin
exp_sbindir = /usr/local/apache2/bin
exp_libdir = /usr/local/apache2/lib
exp_libexecdir = /usr/local/apache2/modules
exp_mandir = /usr/local/apache2/man
exp_sysconfdir = /usr/local/apache2/conf
exp_datadir = /usr/local/apache2
exp_installbuilddir = /usr/local/apache2/build
exp_errordir = /usr/local/apache2/error
exp_iconsdir = /usr/local/apache2/icons
exp_htdocsdir = /usr/local/apache2/htdocs
exp_manualdir = /usr/local/apache2/manual
exp_cgidir = /usr/local/apache2/cgi-bin
exp_includedir = /usr/local/apache2/include
exp_localstatedir = /usr/local/apache2
exp_runtimedir = /usr/local/apache2/logs
exp_logfiledir = /usr/local/apache2/logs
exp_proxycachedir = /usr/local/apache2/proxy
SHLTCFLAGS = -prefer-pic
LTCFLAGS = -prefer-non-pic -static
MKINSTALLDIRS = /usr/local/apache2/build/mkdir.sh
INSTALL = $(LIBTOOL) --mode=install /usr/local/apache2/build/install.sh -c
CRYPT_LIBS = -lcrypt
MPM_NAME = prefork
NONPORTABLE_SUPPORT = checkgid
INSTALL_DSO = yes
progname = httpd
OS = unix
SHLIBPATH_VAR = LD_LIBRARY_PATH
AP_BUILD_SRCLIB_DIRS = apr apr-util pcre
AP_CLEAN_SRCLIB_DIRS = apr-util apr pcre
bindir = ${exec_prefix}/bin
sbindir = ${exec_prefix}/bin
cgidir = ${datadir}/cgi-bin
logfiledir = ${localstatedir}/logs
exec_prefix = ${prefix}
datadir = ${prefix}
localstatedir = ${prefix}
mandir = ${prefix}/man
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/modules
htdocsdir = ${datadir}/htdocs
manualdir = ${datadir}/manual
includedir = ${prefix}/include
errordir = ${datadir}/error
iconsdir = ${datadir}/icons
sysconfdir = ${prefix}/conf
installbuilddir = ${datadir}/build
runtimedir = ${localstatedir}/logs
proxycachedir = ${localstatedir}/proxy
other_targets =
progname = httpd
prefix = /usr/local/apache2
AWK = gawk
CC = gcc
CPP = gcc -E
CXX =
CPPFLAGS =
CFLAGS =
CXXFLAGS =
LTFLAGS = --silent
LDFLAGS =
LT_LDFLAGS =
SH_LDFLAGS =
LIBS =
DEFS =
INCLUDES =
NOTEST_CPPFLAGS =
NOTEST_CFLAGS =
NOTEST_CXXFLAGS =
NOTEST_LDFLAGS =
NOTEST_LIBS =
EXTRA_CPPFLAGS = -DLINUX -D_REENTRANT -D_GNU_SOURCE
EXTRA_CFLAGS = -g -O2 -pthread
EXTRA_CXXFLAGS =
EXTRA_LDFLAGS =
EXTRA_LIBS = -lm
EXTRA_INCLUDES = -I$(includedir) -I. -I/home/project3/httpd-2.2.29/srclib/apr/include -I/home/project3/httpd-2.2.29/srclib/apr-util/include -I/home/project3/httpd-2.2.29/srclib/apr-util/xml/expat/lib
LIBTOOL = /usr/local/apache2/build/libtool --silent
SHELL = /bin/sh
RSYNC = /bin/rsync
SH_LIBS =
SH_LIBTOOL = $(LIBTOOL)
MK_IMPLIB =
MKDEP = $(CC) -MM
INSTALL_PROG_FLAGS =
APR_BINDIR = /usr/local/apache2/bin
APR_INCLUDEDIR = /usr/local/apache2/include
APR_VERSION = 1.5.1
APR_CONFIG = /usr/local/apache2/bin/apr-1-config
APU_BINDIR = /usr/local/apache2/bin
APU_INCLUDEDIR = /usr/local/apache2/include
APU_VERSION = 1.5.3
APU_CONFIG = /usr/local/apache2/bin/apu-1-config