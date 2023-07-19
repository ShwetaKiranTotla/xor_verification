# A packet consists of header and payload.
# Header may or may not contain vlan tag.
# Packets with vlan tag have size of 16 bytes otherwise 14 bytes.
# Packets have different ethertypes min ethertype is 0x800 max is 0xffff
# Packets with ethertype 0x806 have a size of 64

import constraint
import random

class PacketGenerator:
	def __init__(self):
		self.p = constraint.Problem()
		self.p.addVariable('hdrlen', [14,16])
		self.p.addVariable('payload', range(50,1500))
		self.p.addVariable('length', range(64,1500))
		self.p.addVariable('type', range(0x800,0xffff))
		self.p.addVariable('hasVlan', [True, False])
		self.p.addConstraint(lambda len, hdr, pdl: len==hdr+pdl, ['length', 'hdrlen', 'payload'])
		self.p.addConstraint(lambda vlan, hdrlen: hdrlen==16 if vlan else hdrlen==14, ['hasVlan', 'hdrlen'])
		self.p.addConstraint(lambda ethtype: ethtype<=0x810, ['type'])
		self.p.addConstraint(lambda type, len: len==64 if type ==0x806 else True, ['length','type'])
		
	def solve(self):
		self.solutions = self.p.getSolutions()
	def get(self):
		return random.choice(self.solutions)
		
if __name__ == "__main__":
	pkt = PacketGenerator()
	pkt.solve()
	for i in range(5):
		print(f"{pkt.get()}")
