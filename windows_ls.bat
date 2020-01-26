@ECHO OFF
doskey ls=dir /b $*
doskey ll=dir $*
doskey cat=type $*
doskey ..=cd..
doskey grep=find "$1" $2
doskey mv=ren $*
doskey rm=del $*

cd Desktop

@echo Windows LS, LL.
