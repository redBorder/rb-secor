#!/bin/bash

#######################################################################
# Copyright (c) 2014 ENEO Tecnología S.L.
# This file is part of redBorder.
# redBorder is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# redBorder is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License License for more details.
# You should have received a copy of the GNU Affero General Public License License
# along with redBorder. If not, see <http://www.gnu.org/licenses/>.
#######################################################################

cd /var/secor
source /etc/sysconfig/secor

SECOR_JAR=$(find /usr/lib/secor -name "secor-*.jar" | head -n 1)
RB_SECOR_JAR=$(find /var/secor/ -name "rb-secor-*.jar" | head -n 1 | xargs basename)

exec java -Xmx${MEMTOTAL}k -Xms${MEMTOTAL}k -ea -Dsecor_group=secor_partition \
  -Dlog4j.configuration=log4j.prod.properties \
  -Dconfig=secor.prod.partition.properties \
  -cp ${SECOR_JAR}:/var/secor:/var/secor/*:/var/secor/lib/*:${RB_SECOR_JAR} \
  com.pinterest.secor.main.ConsumerMain