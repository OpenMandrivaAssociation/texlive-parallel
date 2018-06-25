# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/parallel
# catalog-date 2007-01-12 20:52:49 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-parallel
Version:	20180303
Release:	1
Summary:	Typeset parallel texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parallel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parallel.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070112-2
+ Revision: 754643
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070112-1
+ Revision: 719191
- texlive-parallel
- texlive-parallel
- texlive-parallel
- texlive-parallel

