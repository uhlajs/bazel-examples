#!/usr/bin/env bash
set -o nounset -o errexit -o pipefail

set -o xtrace
bazel --bazelrc=.aspect/bazelrc/ci.bazelrc clean --expunge
bazel --bazelrc=.aspect/bazelrc/ci.bazelrc build ...
bazel --bazelrc=.aspect/bazelrc/ci.bazelrc test ...
bazel --bazelrc=.aspect/bazelrc/ci.bazelrc query ...
bazel --bazelrc=.aspect/bazelrc/ci.bazelrc fetch ...