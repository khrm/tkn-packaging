%define debug_package %{nil}
%define repo github.com/tektoncd/cli
%if ! 0%{?gobuild:1}
%global gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif
Name:           tkn
Version:        0.1.2
Release:        1%{?dist}
Summary:        A CLI for interacting with Tekton!
License:        Apache 2.0
URL:            https://%{repo}

%{?go_compiler:BuildRequires: compiler(go-compiler)}
BuildRequires: golang >= 1.10
BuildRequires: git

%global import_path github.com/tektoncd/cli

Source0:        https://%{repo}/archive/v%{version}.tar.gz

%description
The Tekton Pipelines cli project provides a CLI for interacting with Tekton !

# vendored libraries (Source0)
Provides: bundled(golang(cloud.google.com/go/compute/metadata)) = v0.37.2
Provides: bundled(golang(cloud.google.com/go/monitoring/apiv3)) = v0.37.2
Provides: bundled(golang(cloud.google.com/go/trace/apiv2)) = v0.37.2
Provides: bundled(golang(contrib.go.opencensus.io/exporter/ocagent)) = v0.2.0
Provides: bundled(golang(contrib.go.opencensus.io/exporter/stackdriver)) = v0.9.1
Provides: bundled(golang(contrib.go.opencensus.io/exporter/stackdriver/monitoredresource)) = v0.9.1
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/services/containerregistry/mgmt/2017-10-01/containerregistry)) = v26.1.0
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/version)) = v26.1.0
Provides: bundled(golang(github.com/Azure/go-autorest/autorest/adal)) = v11.6.0
Provides: bundled(golang(github.com/Azure/go-autorest/autorest/azure)) = v11.6.0
Provides: bundled(golang(github.com/Azure/go-autorest/autorest/date)) = v11.6.0
Provides: bundled(golang(github.com/Azure/go-autorest/autorest/to)) = v11.6.0
Provides: bundled(golang(github.com/Azure/go-autorest/autorest/validation)) = v11.6.0
Provides: bundled(golang(github.com/Azure/go-autorest/tracing)) = v11.6.0
Provides: bundled(golang(github.com/Azure/go-autorest/logger)) = v11.6.0
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/request)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/session)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/ecr)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/ec2metadata)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awserr)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/endpoints)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkio)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/awsutil)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client/metadata)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/client)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/corehandlers)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/processcreds)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/stscreds)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/csm)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/defaults)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/ini)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/shareddefaults)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/signer/v4)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/jsonrpc)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkuri)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/internal/sdkrand)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/service/sts)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/ec2rolecreds)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/aws/credentials/endpointcreds)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/rest)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/json/jsonutil)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/query/queryutil)) = v1.19.11
Provides: bundled(golang(github.com/aws/aws-sdk-go/private/protocol/xml/xmlutil)) = v1.19.11
Provides: bundled(golang(github.com/beorn7/perks/quantile)) = 56c1def75689cceec1fa6f14c2eedb4b798827f9
Provides: bundled(golang(github.com/census-instrumentation/opencensus-proto/gen-go/agent/common/v1)) = v0.1.0
Provides: bundled(golang(github.com/census-instrumentation/opencensus-proto/gen-go/metrics/v1)) = v0.1.0
Provides: bundled(golang(github.com/census-instrumentation/opencensus-proto/gen-go/resource/v1)) = v0.1.0
Provides: bundled(golang(github.com/census-instrumentation/opencensus-proto/gen-go/agent/trace/v1)) = v0.1.0
Provides: bundled(golang(github.com/census-instrumentation/opencensus-proto/gen-go/trace/v1)) = v0.1.0
Provides: bundled(golang(github.com/davecgh/go-spew)) = v1.1.1
Provides: bundled(golang(github.com/dgrijalva/jwt-go)) = v3.2.0
Provides: bundled(golang(github.com/evanphx/json-patch)) = v4.1.0
Provides: bundled(golang(github.com/fatih/color)) = v1.7.0
Provides: bundled(golang(github.com/ghodss/yaml)) = v1.0.0
Provides: bundled(golang(github.com/gogo/protobuf/proto)) = v1.2.0
Provides: bundled(golang(github.com/gogo/protobuf/sortkeys)) = v1.2.0
Provides: bundled(golang(github.com/golang/glog)) = 23def4e6c14b4da8ac2ed8007337bc5eb5007998
Provides: bundled(golang(github.com/golang/protobuf/proto)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/ptypes/any)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/ptypes)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/ptypes/timestamp)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/ptypes/wrappers)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/ptypes/duration)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/ptypes/struct)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/ptypes/empty)) = v1.2.0
Provides: bundled(golang(github.com/golang/protobuf/protoc-gen-go/descriptor)) = v1.2.0
Provides: bundled(golang(github.com/google/btree)) = 4030bb1f1f0c35b30ca7009e9ebd06849dd45306
Provides: bundled(golang(github.com/google/go-cmp/cmp)) = v0.2.0
Provides: bundled(golang(github.com/google/go-cmp/cmp/internal/diff)) = v0.2.0
Provides: bundled(golang(github.com/google/go-cmp/cmp/internal/function)) = v0.2.0
Provides: bundled(golang(github.com/google/go-cmp/cmp/internal/value)) = v0.2.0
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/authn)) =
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/authn/k8schain))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/name))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/v1))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/v1/remote))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/v1/types))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/v1/partial))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/v1/remote/transport))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/v1/stream))
Provides: bundled(golang(github.com/google/go-containerregistry/pkg/v1/v1util))
Provides: bundled(golang(github.com/google/gofuzz))
Provides: bundled(golang(github.com/googleapis/gax-go/v2))
Provides: bundled(golang(github.com/googleapis/gnostic/OpenAPIv2))
Provides: bundled(golang(github.com/googleapis/gnostic/compiler))
Provides: bundled(golang(github.com/googleapis/gnostic/extensions))
Provides: bundled(golang(github.com/gregjones/httpcache))
Provides: bundled(golang(github.com/gregjones/httpcache/diskcache))
Provides: bundled(golang(github.com/hako/durafmt))
Provides: bundled(golang(github.com/hashicorp/golang-lru))
Provides: bundled(golang(github.com/hashicorp/golang-lru/simplelru))
Provides: bundled(golang(github.com/imdario/mergo))
Provides: bundled(golang(github.com/inconshreveable/mousetrap))
Provides: bundled(golang(github.com/jmespath/go-jmespath))
Provides: bundled(golang(github.com/jonboulle/clockwork))
Provides: bundled(golang(github.com/json-iterator/go))
Provides: bundled(golang(github.com/knative/pkg/apis))
Provides: bundled(golang(github.com/knative/pkg/apis/duck/v1beta1))
Provides: bundled(golang(github.com/knative/pkg/apis/duck))
Provides: bundled(golang(github.com/knative/pkg/controller))
Provides: bundled(golang(github.com/knative/pkg/test))
Provides: bundled(golang(github.com/knative/pkg/test/logging))
Provides: bundled(golang(github.com/knative/pkg/kmp))
Provides: bundled(golang(github.com/knative/pkg/kmeta))
Provides: bundled(golang(github.com/knative/pkg/logging))
Provides: bundled(golang(github.com/knative/pkg/logging/logkey))
Provides: bundled(golang(github.com/knative/pkg/metrics))
Provides: bundled(golang(github.com/knative/pkg/test/spoof))
Provides: bundled(golang(github.com/knative/pkg/changeset))
Provides: bundled(golang(github.com/knative/pkg/metrics/metricskey))
Provides: bundled(golang(github.com/knative/pkg/test/ingress))
Provides: bundled(golang(github.com/knative/pkg/test/zipkin))
Provides: bundled(golang(github.com/knative/pkg/test/monitoring))
Provides: bundled(golang(github.com/mattbaird/jsonpatch))
Provides: bundled(golang(github.com/mattn/go-colorable))
Provides: bundled(golang(github.com/mattn/go-isatty))
Provides: bundled(golang(github.com/matttproud/golang_protobuf_extensions/pbutil))
Provides: bundled(golang(github.com/modern-go/concurrent))
Provides: bundled(golang(github.com/modern-go/reflect2))
Provides: bundled(golang(github.com/peterbourgon/diskv))
Provides: bundled(golang(github.com/pkg/errors))
Provides: bundled(golang(github.com/prometheus/client_golang/prometheus))
Provides: bundled(golang(github.com/prometheus/client_golang/prometheus/promhttp))
Provides: bundled(golang(github.com/prometheus/client_golang/prometheus/internal))
Provides: bundled(golang(github.com/prometheus/client_model/go))
Provides: bundled(golang(github.com/prometheus/common/expfmt))
Provides: bundled(golang(github.com/prometheus/common/model))
Provides: bundled(golang(github.com/prometheus/common/internal/bitbucket.org/ww/goautoneg))
Provides: bundled(golang(github.com/prometheus/procfs))
Provides: bundled(golang(github.com/prometheus/procfs/iostats))
Provides: bundled(golang(github.com/prometheus/procfs/nfs))
Provides: bundled(golang(github.com/prometheus/procfs/xfs))
Provides: bundled(golang(github.com/prometheus/procfs/internal/util))
Provides: bundled(golang(github.com/spf13/cobra))
Provides: bundled(golang(github.com/spf13/pflag))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/apis/pipeline/v1alpha1))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/reconciler/v1alpha1/taskrun/resources))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/informers/externalversions))
Provides: bundled(golang(github.com/tektoncd/pipeline/test/builder))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned/typed/pipeline/v1alpha1))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/apis/pipeline))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/list))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/names))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/templating))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/reconciler/v1alpha1/pipelinerun/resources))
Provides: bundled(golang(github.com/tektoncd/pipeline/test))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/artifacts))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/listers/pipeline/v1alpha1))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/credentials))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/credentials/dockercreds))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/credentials/gitcreds))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/merge))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/reconciler/v1alpha1/taskrun/entrypoint))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/informers/externalversions/internalinterfaces))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/informers/externalversions/pipeline))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned/scheme))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned/fake))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/informers/externalversions/pipeline/v1alpha1))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/system))
Provides: bundled(golang(github.com/tektoncd/pipeline/pkg/client/clientset/versioned/typed/pipeline/v1alpha1/fake))
Provides: bundled(golang(github.com/tektoncd/plumbing/scripts))
Provides: bundled(golang(go.opencensus.io/trace))
Provides: bundled(golang(go.opencensus.io/stats))
Provides: bundled(golang(go.opencensus.io/stats/view))
Provides: bundled(golang(go.opencensus.io/tag))
Provides: bundled(golang(go.opencensus.io/exemplar))
Provides: bundled(golang(go.opencensus.io/internal))
Provides: bundled(golang(go.opencensus.io/trace/internal))
Provides: bundled(golang(go.opencensus.io/trace/tracestate))
Provides: bundled(golang(go.opencensus.io/exporter/prometheus))
Provides: bundled(golang(go.opencensus.io/stats/internal))
Provides: bundled(golang(go.opencensus.io/internal/tagencoding))
Provides: bundled(golang(go.opencensus.io/plugin/ochttp))
Provides: bundled(golang(go.opencensus.io/plugin/ochttp/propagation/b3))
Provides: bundled(golang(go.opencensus.io))
Provides: bundled(golang(go.opencensus.io/trace/propagation))
Provides: bundled(golang(go.opencensus.io/plugin/ochttp/propagation/tracecontext))
Provides: bundled(golang(go.opencensus.io/plugin/ocgrpc))
Provides: bundled(golang(go.uber.org/atomic))
Provides: bundled(golang(go.uber.org/multierr))
Provides: bundled(golang(go.uber.org/zap))
Provides: bundled(golang(go.uber.org/zap/zaptest/observer))
Provides: bundled(golang(go.uber.org/zap/internal/bufferpool))
Provides: bundled(golang(go.uber.org/zap/zapcore))
Provides: bundled(golang(go.uber.org/zap/buffer))
Provides: bundled(golang(go.uber.org/zap/internal/color))
Provides: bundled(golang(go.uber.org/zap/internal/exit))
Provides: bundled(golang(golang.org/x/crypto/ssh/terminal))
Provides: bundled(golang(golang.org/x/crypto/pkcs12))
Provides: bundled(golang(golang.org/x/crypto/pkcs12/internal/rc2))
Provides: bundled(golang(golang.org/x/net/http2))
Provides: bundled(golang(golang.org/x/net/http/httpguts))
Provides: bundled(golang(golang.org/x/net/http2/hpack))
Provides: bundled(golang(golang.org/x/net/idna))
Provides: bundled(golang(golang.org/x/net/context/ctxhttp))
Provides: bundled(golang(golang.org/x/net/context))
Provides: bundled(golang(golang.org/x/net/trace))
Provides: bundled(golang(golang.org/x/net/internal/timeseries))
Provides: bundled(golang(golang.org/x/oauth2))
Provides: bundled(golang(golang.org/x/oauth2/google))
Provides: bundled(golang(golang.org/x/oauth2/internal))
Provides: bundled(golang(golang.org/x/oauth2/jws))
Provides: bundled(golang(golang.org/x/oauth2/jwt))
Provides: bundled(golang(golang.org/x/sync/errgroup))
Provides: bundled(golang(golang.org/x/sync/semaphore))
Provides: bundled(golang(golang.org/x/sys/unix))
Provides: bundled(golang(golang.org/x/sys/windows))
Provides: bundled(golang(golang.org/x/text/encoding/unicode))
Provides: bundled(golang(golang.org/x/text/transform))
Provides: bundled(golang(golang.org/x/text/secure/bidirule))
Provides: bundled(golang(golang.org/x/text/unicode/bidi))
Provides: bundled(golang(golang.org/x/text/unicode/norm))
Provides: bundled(golang(golang.org/x/text/encoding))
Provides: bundled(golang(golang.org/x/text/encoding/internal))
Provides: bundled(golang(golang.org/x/text/encoding/internal/identifier))
Provides: bundled(golang(golang.org/x/text/internal/utf8internal))
Provides: bundled(golang(golang.org/x/text/runes))
Provides: bundled(golang(golang.org/x/time/rate))
Provides: bundled(golang(google.golang.org/api/option))
Provides: bundled(golang(google.golang.org/api/support/bundler))
Provides: bundled(golang(google.golang.org/api/iterator))
Provides: bundled(golang(google.golang.org/api/transport))
Provides: bundled(golang(google.golang.org/api/internal))
Provides: bundled(golang(google.golang.org/api/transport/grpc))
Provides: bundled(golang(google.golang.org/api/transport/http))
Provides: bundled(golang(google.golang.org/api/googleapi/transport))
Provides: bundled(golang(google.golang.org/api/transport/http/internal/propagation))
Provides: bundled(golang(google.golang.org/appengine))
Provides: bundled(golang(google.golang.org/appengine/urlfetch))
Provides: bundled(golang(google.golang.org/appengine/internal))
Provides: bundled(golang(google.golang.org/appengine/internal/app_identity))
Provides: bundled(golang(google.golang.org/appengine/internal/modules))
Provides: bundled(golang(google.golang.org/appengine/internal/urlfetch))
Provides: bundled(golang(google.golang.org/appengine/internal/base))
Provides: bundled(golang(google.golang.org/appengine/internal/datastore))
Provides: bundled(golang(google.golang.org/appengine/internal/log))
Provides: bundled(golang(google.golang.org/appengine/internal/remote_api))
Provides: bundled(golang(google.golang.org/appengine/socket))
Provides: bundled(golang(google.golang.org/appengine/internal/socket))
Provides: bundled(golang(google.golang.org/genproto/googleapis/api/distribution))
Provides: bundled(golang(google.golang.org/genproto/googleapis/api/label))
Provides: bundled(golang(google.golang.org/genproto/googleapis/api/metric))
Provides: bundled(golang(google.golang.org/genproto/googleapis/api/monitoredres))
Provides: bundled(golang(google.golang.org/genproto/googleapis/devtools/cloudtrace/v2))
Provides: bundled(golang(google.golang.org/genproto/googleapis/monitoring/v3))
Provides: bundled(golang(google.golang.org/genproto/googleapis/rpc/status))
Provides: bundled(golang(google.golang.org/genproto/googleapis/api))
Provides: bundled(golang(google.golang.org/genproto/googleapis/api/annotations))
Provides: bundled(golang(google.golang.org/genproto/protobuf/field_mask))
Provides: bundled(golang(google.golang.org/grpc))
Provides: bundled(golang(google.golang.org/grpc/codes))
Provides: bundled(golang(google.golang.org/grpc/metadata))
Provides: bundled(golang(google.golang.org/grpc/status))
Provides: bundled(golang(google.golang.org/grpc/balancer))
Provides: bundled(golang(google.golang.org/grpc/balancer/roundrobin))
Provides: bundled(golang(google.golang.org/grpc/connectivity))
Provides: bundled(golang(google.golang.org/grpc/credentials))
Provides: bundled(golang(google.golang.org/grpc/encoding))
Provides: bundled(golang(google.golang.org/grpc/encoding/proto))
Provides: bundled(golang(google.golang.org/grpc/grpclog))
Provides: bundled(golang(google.golang.org/grpc/internal))
Provides: bundled(golang(google.golang.org/grpc/internal/backoff))
Provides: bundled(golang(google.golang.org/grpc/internal/binarylog))
Provides: bundled(golang(google.golang.org/grpc/internal/channelz))
Provides: bundled(golang(google.golang.org/grpc/internal/envconfig))
Provides: bundled(golang(google.golang.org/grpc/internal/grpcrand))
Provides: bundled(golang(google.golang.org/grpc/internal/grpcsync))
Provides: bundled(golang(google.golang.org/grpc/internal/transport))
Provides: bundled(golang(google.golang.org/grpc/keepalive))
Provides: bundled(golang(google.golang.org/grpc/naming))
Provides: bundled(golang(google.golang.org/grpc/peer))
Provides: bundled(golang(google.golang.org/grpc/resolver))
Provides: bundled(golang(google.golang.org/grpc/resolver/dns))
Provides: bundled(golang(google.golang.org/grpc/resolver/passthrough))
Provides: bundled(golang(google.golang.org/grpc/stats))
Provides: bundled(golang(google.golang.org/grpc/tap))
Provides: bundled(golang(google.golang.org/grpc/credentials/oauth))
Provides: bundled(golang(google.golang.org/grpc/balancer/base))
Provides: bundled(golang(google.golang.org/grpc/credentials/internal))
Provides: bundled(golang(google.golang.org/grpc/binarylog/grpc_binarylog_v1))
Provides: bundled(golang(google.golang.org/grpc/internal/syscall))
Provides: bundled(golang(gopkg.in/inf.v0))
Provides: bundled(golang(gopkg.in/yaml.v2))
Provides: bundled(golang(k8s.io/api/core/v1))
Provides: bundled(golang(k8s.io/api/authentication/v1))
Provides: bundled(golang(k8s.io/api/admissionregistration/v1alpha1))
Provides: bundled(golang(k8s.io/api/admissionregistration/v1beta1))
Provides: bundled(golang(k8s.io/api/apps/v1))
Provides: bundled(golang(k8s.io/api/apps/v1beta1))
Provides: bundled(golang(k8s.io/api/apps/v1beta2))
Provides: bundled(golang(k8s.io/api/autoscaling/v1))
Provides: bundled(golang(k8s.io/api/autoscaling/v2beta1))
Provides: bundled(golang(k8s.io/api/autoscaling/v2beta2))
Provides: bundled(golang(k8s.io/api/batch/v1))
Provides: bundled(golang(k8s.io/api/batch/v1beta1))
Provides: bundled(golang(k8s.io/api/batch/v2alpha1))
Provides: bundled(golang(k8s.io/api/certificates/v1beta1))
Provides: bundled(golang(k8s.io/api/coordination/v1beta1))
Provides: bundled(golang(k8s.io/api/events/v1beta1))
Provides: bundled(golang(k8s.io/api/extensions/v1beta1))
Provides: bundled(golang(k8s.io/api/networking/v1))
Provides: bundled(golang(k8s.io/api/policy/v1beta1))
Provides: bundled(golang(k8s.io/api/rbac/v1))
Provides: bundled(golang(k8s.io/api/rbac/v1alpha1))
Provides: bundled(golang(k8s.io/api/rbac/v1beta1))
Provides: bundled(golang(k8s.io/api/scheduling/v1alpha1))
Provides: bundled(golang(k8s.io/api/scheduling/v1beta1))
Provides: bundled(golang(k8s.io/api/settings/v1alpha1))
Provides: bundled(golang(k8s.io/api/storage/v1))
Provides: bundled(golang(k8s.io/api/storage/v1alpha1))
Provides: bundled(golang(k8s.io/api/storage/v1beta1))
Provides: bundled(golang(k8s.io/api/authentication/v1beta1))
Provides: bundled(golang(k8s.io/api/authorization/v1))
Provides: bundled(golang(k8s.io/api/authorization/v1beta1))
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/schema))
Provides: bundled(golang(k8s.io/apimachinery/pkg/fields))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/net))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/yaml))
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/errors))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/streaming))
Provides: bundled(golang(k8s.io/apimachinery/pkg/types))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/sets))
Provides: bundled(golang(k8s.io/apimachinery/pkg/watch))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/errors))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/validation))
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/equality))
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/resource))
Provides: bundled(golang(k8s.io/apimachinery/pkg/conversion))
Provides: bundled(golang(k8s.io/apimachinery/pkg/labels))
Provides: bundled(golang(k8s.io/apimachinery/pkg/selection))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/intstr))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/runtime))
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/meta))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/json))
Provides: bundled(golang(k8s.io/apimachinery/pkg/api/validation))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/cache))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/clock))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/diff))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/naming))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/wait))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer))
Provides: bundled(golang(k8s.io/apimachinery/pkg/conversion/queryparams))
Provides: bundled(golang(k8s.io/apimachinery/pkg/version))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/validation/field))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/json))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/versioning))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/rand))
Provides: bundled(golang(k8s.io/apimachinery/third_party/forked/golang/reflect))
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1beta1))
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured))
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured/unstructuredscheme))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/strategicpatch))
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/v1/validation))
Provides: bundled(golang(k8s.io/apimachinery/pkg/apis/meta/internalversion))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/protobuf))
Provides: bundled(golang(k8s.io/apimachinery/pkg/runtime/serializer/recognizer))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/framer))
Provides: bundled(golang(k8s.io/apimachinery/pkg/util/mergepatch))
Provides: bundled(golang(k8s.io/apimachinery/third_party/forked/golang/json))
Provides: bundled(golang(k8s.io/cli-runtime/pkg/genericclioptions))
Provides: bundled(golang(k8s.io/cli-runtime/pkg/genericclioptions/printers))
Provides: bundled(golang(k8s.io/cli-runtime/pkg/genericclioptions/resource))
Provides: bundled(golang(k8s.io/client-go/plugin/pkg/client/auth/gcp))
Provides: bundled(golang(k8s.io/client-go/plugin/pkg/client/auth/oidc))
Provides: bundled(golang(k8s.io/client-go/kubernetes))
Provides: bundled(golang(k8s.io/client-go/rest))
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd))
Provides: bundled(golang(k8s.io/client-go/tools/cache))
Provides: bundled(golang(k8s.io/client-go/informers))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/core/v1))
Provides: bundled(golang(k8s.io/client-go/util/jsonpath))
Provides: bundled(golang(k8s.io/client-go/discovery))
Provides: bundled(golang(k8s.io/client-go/util/flowcontrol))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta2))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v2beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v2beta2))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v2alpha1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/certificates/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/coordination/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/events/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/extensions/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/networking/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/policy/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/scheduling/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/scheduling/v1beta1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/settings/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1beta1))
Provides: bundled(golang(k8s.io/client-go/pkg/version))
Provides: bundled(golang(k8s.io/client-go/plugin/pkg/client/auth/exec))
Provides: bundled(golang(k8s.io/client-go/rest/watch))
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api))
Provides: bundled(golang(k8s.io/client-go/tools/metrics))
Provides: bundled(golang(k8s.io/client-go/transport))
Provides: bundled(golang(k8s.io/client-go/util/cert))
Provides: bundled(golang(k8s.io/client-go/tools/auth))
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api/latest))
Provides: bundled(golang(k8s.io/client-go/util/homedir))
Provides: bundled(golang(k8s.io/client-go/restmapper))
Provides: bundled(golang(k8s.io/client-go/testing))
Provides: bundled(golang(k8s.io/client-go/tools/pager))
Provides: bundled(golang(k8s.io/client-go/util/buffer))
Provides: bundled(golang(k8s.io/client-go/util/retry))
Provides: bundled(golang(k8s.io/client-go/informers/admissionregistration))
Provides: bundled(golang(k8s.io/client-go/informers/apps))
Provides: bundled(golang(k8s.io/client-go/informers/autoscaling))
Provides: bundled(golang(k8s.io/client-go/informers/batch))
Provides: bundled(golang(k8s.io/client-go/informers/certificates))
Provides: bundled(golang(k8s.io/client-go/informers/coordination))
Provides: bundled(golang(k8s.io/client-go/informers/core))
Provides: bundled(golang(k8s.io/client-go/informers/events))
Provides: bundled(golang(k8s.io/client-go/informers/extensions))
Provides: bundled(golang(k8s.io/client-go/informers/internalinterfaces))
Provides: bundled(golang(k8s.io/client-go/informers/networking))
Provides: bundled(golang(k8s.io/client-go/informers/policy))
Provides: bundled(golang(k8s.io/client-go/informers/rbac))
Provides: bundled(golang(k8s.io/client-go/informers/scheduling))
Provides: bundled(golang(k8s.io/client-go/informers/settings))
Provides: bundled(golang(k8s.io/client-go/informers/storage))
Provides: bundled(golang(k8s.io/client-go/kubernetes/scheme))
Provides: bundled(golang(k8s.io/client-go/tools/reference))
Provides: bundled(golang(k8s.io/client-go/third_party/forked/golang/template))
Provides: bundled(golang(k8s.io/client-go/util/integer))
Provides: bundled(golang(k8s.io/client-go/pkg/apis/clientauthentication))
Provides: bundled(golang(k8s.io/client-go/pkg/apis/clientauthentication/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/pkg/apis/clientauthentication/v1beta1))
Provides: bundled(golang(k8s.io/client-go/util/connrotation))
Provides: bundled(golang(k8s.io/client-go/tools/clientcmd/api/v1))
Provides: bundled(golang(k8s.io/client-go/informers/core/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/fake))
Provides: bundled(golang(k8s.io/client-go/informers/admissionregistration/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/informers/admissionregistration/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/apps/v1))
Provides: bundled(golang(k8s.io/client-go/informers/apps/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/apps/v1beta2))
Provides: bundled(golang(k8s.io/client-go/informers/autoscaling/v1))
Provides: bundled(golang(k8s.io/client-go/informers/autoscaling/v2beta1))
Provides: bundled(golang(k8s.io/client-go/informers/autoscaling/v2beta2))
Provides: bundled(golang(k8s.io/client-go/informers/batch/v1))
Provides: bundled(golang(k8s.io/client-go/informers/batch/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/batch/v2alpha1))
Provides: bundled(golang(k8s.io/client-go/informers/certificates/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/coordination/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/events/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/extensions/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/networking/v1))
Provides: bundled(golang(k8s.io/client-go/informers/policy/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/rbac/v1))
Provides: bundled(golang(k8s.io/client-go/informers/rbac/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/informers/rbac/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/scheduling/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/informers/scheduling/v1beta1))
Provides: bundled(golang(k8s.io/client-go/informers/settings/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/informers/storage/v1))
Provides: bundled(golang(k8s.io/client-go/informers/storage/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/informers/storage/v1beta1))
Provides: bundled(golang(k8s.io/client-go/dynamic))
Provides: bundled(golang(k8s.io/client-go/util/workqueue))
Provides: bundled(golang(k8s.io/client-go/discovery/fake))
Provides: bundled(golang(k8s.io/client-go/listers/core/v1))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1alpha1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/admissionregistration/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/apps/v1beta2/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authentication/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/authorization/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v2beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/autoscaling/v2beta2/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/batch/v2alpha1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/certificates/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/coordination/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/core/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/events/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/extensions/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/networking/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/policy/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1alpha1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/rbac/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/scheduling/v1alpha1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/scheduling/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/settings/v1alpha1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1alpha1/fake))
Provides: bundled(golang(k8s.io/client-go/kubernetes/typed/storage/v1beta1/fake))
Provides: bundled(golang(k8s.io/client-go/listers/admissionregistration/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/listers/admissionregistration/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/apps/v1))
Provides: bundled(golang(k8s.io/client-go/listers/apps/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/apps/v1beta2))
Provides: bundled(golang(k8s.io/client-go/listers/autoscaling/v1))
Provides: bundled(golang(k8s.io/client-go/listers/autoscaling/v2beta1))
Provides: bundled(golang(k8s.io/client-go/listers/autoscaling/v2beta2))
Provides: bundled(golang(k8s.io/client-go/listers/batch/v1))
Provides: bundled(golang(k8s.io/client-go/listers/batch/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/batch/v2alpha1))
Provides: bundled(golang(k8s.io/client-go/listers/certificates/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/coordination/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/events/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/extensions/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/networking/v1))
Provides: bundled(golang(k8s.io/client-go/listers/policy/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/rbac/v1))
Provides: bundled(golang(k8s.io/client-go/listers/rbac/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/listers/rbac/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/scheduling/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/listers/scheduling/v1beta1))
Provides: bundled(golang(k8s.io/client-go/listers/settings/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/listers/storage/v1))
Provides: bundled(golang(k8s.io/client-go/listers/storage/v1alpha1))
Provides: bundled(golang(k8s.io/client-go/listers/storage/v1beta1))
Provides: bundled(golang(k8s.io/klog))
Provides: bundled(golang(k8s.io/kube-openapi/pkg/util/proto))
Provides: bundled(golang(k8s.io/kubernetes/pkg/credentialprovider))
Provides: bundled(golang(k8s.io/kubernetes/pkg/credentialprovider/aws))
Provides: bundled(golang(k8s.io/kubernetes/pkg/credentialprovider/azure))
Provides: bundled(golang(k8s.io/kubernetes/pkg/credentialprovider/gcp))
Provides: bundled(golang(k8s.io/kubernetes/pkg/credentialprovider/secrets))
Provides: bundled(golang(k8s.io/kubernetes/pkg/cloudprovider/providers/azure/auth))
Provides: bundled(golang(sigs.k8s.io/yaml))

#BuildRequires: golang(cloud.google.com/go)(commit=458e1f376a2b44413160b5d301183b65debaa3f6)
#BuildRequires: golang(contrib.go.opencensus.io/exporter/ocagent)(commit=00af367e65149ff1f2f4b93bbfbb84fd9297170d)
#BuildRequires: golang(contrib.go.opencensus.io/exporter/stackdriver)(commit=0e2df90c35d1575910dc0a44da7d7b08ae76290f)
#BuildRequires: golang(github.com/Azure/azure-sdk-for-go)(commit=4d7ea88c4dd04df3dff2c3118136a0e1e3bd787d)
#BuildRequires: golang(github.com/Azure/go-autorest/autorest)(commit=808755da8cf643e4b6b44e0117be7e092de0923c)
#BuildRequires: golang(github.com/beorn7/perks/quantile)(commit=56c1def75689cceec1fa6f14c2eedb4b798827f9)
#BuildRequires: golang(github.com/census-instrumentation/opencensus-proto)(commit=3a771d992973f24aa725d07868b467d1ddfceafb)
#BuildRequires: golang(github.com/davecgh/go-spew)(commit=8991bc29aa16c548c550c7ff78260e27b9ab7c73)
#BuildRequires: golang(github.com/dgrijalva/jwt-go)(commit=06ea1031745cb8b3dab3f6a236daf2b0aa468b7e)

%prep
%setup -q -c
cp cli-%{version}/LICENSE LICENSE
mkdir -p $(dirname _build/src/%{import_path})

%build
ln -s $PWD/cli-%{version} _build/src/%{import_path}
export GOPATH="$PWD/_build:%{gopath}"
export LDFLAGS="${LDFLAGS:-} -X %{import_path}/pkg/cmd/version.clientVersion=%{version}"
export PATH=$PATH:"%{_builddir}"/bin

%gobuild -o _bin/tkn %{import_path}/cmd/tkn

%install
install -D -m 0755 _bin/tkn %{buildroot}%{_bindir}/tkn

%files
%license LICENSE
%{_bindir}/tkn

%changelog
* Thu Jun 20 2019 Khurram Baig <kbaig@redhat.com> 0.12
- Initial version of the rpm


