#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A binary protocol generator
Summary(pl.UTF-8):	Generator protokołów binarnych
Name:		ocaml-bin_prot
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/bin_prot/tags
Source0:	https://github.com/janestreet/bin_prot/archive/v%{version}/bin_prot-%{version}.tar.gz
# Source0-md5:	11d8f6dd7b1400f63f1729d2319130b9
URL:		https://github.com/janestreet/bin_prot
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_compare-devel >= 0.14
BuildRequires:	ocaml-ppx_compare-devel < 0.15
BuildRequires:	ocaml-ppx_custom_printf-devel >= 0.14
BuildRequires:	ocaml-ppx_custom_printf-devel < 0.15
BuildRequires:	ocaml-ppx_fields_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_fields_conv-devel < 0.15
BuildRequires:	ocaml-ppx_optcomp-devel >= 0.14
BuildRequires:	ocaml-ppx_optcomp-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppx_variants_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_variants_conv-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generation of fast comparison and equality functions from type
expressions and definitions.

This package contains files needed to run bytecode executables using
bin_prot library.

%description -l pl.UTF-8
Generowanie szybkich funkcji porównujących i przyrównujących z wyrażeń
i definicji typów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki bin_prot.

%package devel
Summary:	A binary protocol generator - development part
Summary(pl.UTF-8):	Generator protokołów binarnych - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_compare-devel >= 0.14
Requires:	ocaml-ppx_custom_printf-devel >= 0.14
Requires:	ocaml-ppx_fields_conv-devel >= 0.14
Requires:	ocaml-ppx_optcomp-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppx_variants_conv-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
bin_prot library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki bin_prot.

%prep
%setup -q -n bin_prot-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/bin_prot/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/bin_prot/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/bin_prot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md CHANGES.txt COPYRIGHT.txt LICENSE.md LICENSE-Tywith.txt README.md THIRD-PARTY.txt TODO.txt
%dir %{_libdir}/ocaml/bin_prot
%{_libdir}/ocaml/bin_prot/META
%{_libdir}/ocaml/bin_prot/runtime.js
%{_libdir}/ocaml/bin_prot/*.cma
%dir %{_libdir}/ocaml/bin_prot/shape
%{_libdir}/ocaml/bin_prot/shape/*.cma
%dir %{_libdir}/ocaml/bin_prot/xen
%{_libdir}/ocaml/bin_prot/xen/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/bin_prot/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/bin_prot/shape/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/bin_prot/xen/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllbin_prot_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/bin_prot/libbin_prot_stubs.a
%{_libdir}/ocaml/bin_prot/*.cmi
%{_libdir}/ocaml/bin_prot/*.cmt
%{_libdir}/ocaml/bin_prot/*.cmti
%{_libdir}/ocaml/bin_prot/*.mli
%{_libdir}/ocaml/bin_prot/shape/*.cmi
%{_libdir}/ocaml/bin_prot/shape/*.cmt
%{_libdir}/ocaml/bin_prot/shape/*.cmti
%{_libdir}/ocaml/bin_prot/shape/*.mli
%{_libdir}/ocaml/bin_prot/xen/*.cmi
%{_libdir}/ocaml/bin_prot/xen/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/bin_prot/bin_prot.a
%{_libdir}/ocaml/bin_prot/*.cmx
%{_libdir}/ocaml/bin_prot/*.cmxa
%{_libdir}/ocaml/bin_prot/shape/bin_shape_lib.a
%{_libdir}/ocaml/bin_prot/shape/*.cmx
%{_libdir}/ocaml/bin_prot/shape/*.cmxa
%{_libdir}/ocaml/bin_prot/xen/bin_prot_xen.a
%{_libdir}/ocaml/bin_prot/xen/*.cmx
%{_libdir}/ocaml/bin_prot/xen/*.cmxa
%endif
%{_libdir}/ocaml/bin_prot/dune-package
%{_libdir}/ocaml/bin_prot/opam
