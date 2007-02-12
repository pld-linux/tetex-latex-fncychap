
%define	short_name	fncychap
%define	texhash		[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Six fancy chapter styles
Summary(pl.UTF-8):   Sześć eleganckich stylów dla rozdziałów
Name:		tetex-latex-%{short_name}
Version:	1.33
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	ftp://cam.ctan.org/tex-archive/macros/latex/contrib/fncychap.zip
# Source0-md5:	626535090eb82a4c14180b7561f31921
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package contains six fancy chapter styles to use in your LaTeX
documents.

%description -l pl.UTF-8
Pakiet zawiera sześć ozdobnych stylów rozdziałów do używania w
dokumentach LaTeXowych.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{short_name}.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc fncychap.pdf readme.txt
%{_datadir}/texmf/tex/latex/%{short_name}
