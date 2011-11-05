# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/parallel
# catalog-date 2007-01-12 20:52:49 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-parallel
Version:	20070112
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides a parallel environment which allows two potentially
different texts to be typeset in two columns, while maintaining
alignment. The two columns may be on the same page, or on
facing pages. This arrangement of text is commonly used when
typesetting translations, but it can have value when comparing
any two texts.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
