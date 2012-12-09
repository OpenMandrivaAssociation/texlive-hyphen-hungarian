# revision 23085
# category TLCore
# catalog-ctan /language/hungarian/hyphenation
# catalog-date 2009-09-27 14:03:04 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-hyphen-hungarian
Version:	20090927
Release:	3
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
\%% from hyphen-hungarian:
hungarian loadhyph-hu.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-hungarian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-hungarian <<EOF
\%% from hyphen-hungarian:
\addlanguage{hungarian}{loadhyph-hu.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-hungarian
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


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090927-3
+ Revision: 767556
- Add workaround to rpm bug that broke hyphenation files
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090927-2
+ Revision: 759917
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090927-1
+ Revision: 718659
- texlive-hyphen-hungarian
- texlive-hyphen-hungarian
- texlive-hyphen-hungarian
- texlive-hyphen-hungarian

