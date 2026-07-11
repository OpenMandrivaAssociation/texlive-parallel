%global tl_name parallel
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset parallel texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/parallel
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a parallel environment which allows two potentially different
texts to be typeset in two columns, while maintaining alignment. The two
columns may be on the same page, or on facing pages. This arrangement of
text is commonly used when typesetting translations, but it can have
value when comparing any two texts.

