%global tl_name parades
%global tl_revision 40042

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Tabulators and space between paragraphs in galley approach
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/parades
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parades.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/parades.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LaTeX package paravesp controls the spaces above and below
paragraphs. The python script parades.py generates paragraph styles with
support of space above, space below and tabulators. The system imposes
the galley approach on the document.

