
%define	short_name	fncychap
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Six fancy chapter styles
Summary(pl):	Sze¶æ eleganckich stylów dla rozdzia³ów
Name:		tetex-latex-%{short_name}
Version:	1.11
Release:	2
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	ftp://cam.ctan.org/tex-archive/macros/latex/contrib/fncychap/fncychap.sty
Source1:	ftp://cam.ctan.org/tex-archive/macros/latex/contrib/fncychap/fncychap.ps
# ftp://cam.ctan.org/tex-archive/macros/latex/contrib/fncychap/readme.txt
Source2:	%{name}.readme	
Requires:	tetex-latex
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package modifies the tabularx environment to combine the features
of the tabularx package (auto-sized columns in a fixed width table)
with those of the longtable package (multi-page tables).

%description -l pl
Pakiet modyfikuje ¶rodowisko tabularx ³±cz±c cechy pakietu tabularx
(automatyczna szeroko¶æ kolumn w tabeli o narzuconej szeroko¶ci) z
cechami pakietu longtable (wielostronicowe tabele).

%prep
%setup -c -T -q 
install %{SOURCE1} .
install %{SOURCE2} readme.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc fncychap.ps readme.txt
%{_datadir}/texmf/tex/latex/%{short_name}
