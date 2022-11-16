Name:		texlive-parades
Version:	40042
Release:	1
Summary:	Tabulators and space between paragraphs in galley approach
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parades
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parades.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parades.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The LaTeX package paravesp controls the spaces above and below
paragraphs. The python script parades.py generates paragraph
styles with support of space above, space below and tabulators.
The system imposes the galley approach on the document.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/parades
%doc %{_texmfdistdir}/doc/latex/parades

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
