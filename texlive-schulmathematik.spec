Name:		texlive-schulmathematik
Version:	67426
Release:	1
Summary:	Commands and document classes for German-speaking teachers of mathematics and physics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/schulmathematik
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schulmathematik.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schulmathematik.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The schulmathematik bundle provides two LaTeX packages and six
document classes for German-speaking teachers of mathematics
and physics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/schulmathematik
%doc %{_texmfdistdir}/doc/latex/schulmathematik

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
