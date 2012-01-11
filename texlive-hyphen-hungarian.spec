# revision 23085
# category TLCore
# catalog-ctan /language/hungarian/hyphenation
# catalog-date 2009-09-27 14:03:04 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-hyphen-hungarian
Version:	20090927
Release:	2
Summary:	Hungarian hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hungarian/hyphenation
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-hungarian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-hungarian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Hungarian in T1/EC and UTF-8
encodings. From https://github.com/nagybence/huhyphn/.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-hungarian
%_texmf_language_def_d/hyphen-hungarian
%_texmf_language_lua_d/hyphen-hungarian
%doc %{_texmfdir}/doc/generic/huhyphen/huhyphn.pdf
%doc %{_texmfdir}/doc/generic/huhyphen/hyph_hu.dic
%doc %{_texmfdir}/doc/generic/huhyphen/searchforerrors.rb
%doc %{_texmfdir}/doc/generic/huhyphen/testhyphenation.rb

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-hungarian <<EOF
\%\% from hyphen-hungarian:
hungarian loadhyph-hu.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-hungarian <<EOF
\%\% from hyphen-hungarian:
\addlanguage{hungarian}{loadhyph-hu.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-hungarian <<EOF
-- from hyphen-hungarian:
	['hungarian'] = {
		loader = 'loadhyph-hu.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-hu.pat.txt',
		hyphenation = '',
	},
EOF
