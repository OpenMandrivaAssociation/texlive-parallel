Name:		texlive-parallel
Version:	15878
Release:	2
Summary:	Typeset parallel texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parallel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a parallel environment which allows two potentially
different texts to be typeset in two columns, while maintaining
alignment. The two columns may be on the same page, or on
facing pages. This arrangement of text is commonly used when
typesetting translations, but it can have value when comparing
any two texts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parallel/parallel.sty
%doc %{_texmfdistdir}/doc/latex/parallel/example1.tex
%doc %{_texmfdistdir}/doc/latex/parallel/example2.tex
%doc %{_texmfdistdir}/doc/latex/parallel/parallel.pdf
%doc %{_texmfdistdir}/doc/latex/parallel/readme
#- source
%doc %{_texmfdistdir}/source/latex/parallel/parallel.drv
%doc %{_texmfdistdir}/source/latex/parallel/parallel.dtx
%doc %{_texmfdistdir}/source/latex/parallel/parallel.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
