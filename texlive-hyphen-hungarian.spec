%global tl_name hyphen-hungarian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Hungarian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hungarian/hyphenation
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-hungarian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-hungarian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Hungarian in T1/EC and UTF-8 encodings.

