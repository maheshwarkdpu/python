#ifndef _CAVIUM_ECC_DATA_H_
#define _CAVIUM_ECC_DATA_H_
#include <stdint.h>
void n5_bignum_prep(unsigned char* str, int modlength, int z);
struct curve_data {
	unsigned char prime[256];
	unsigned char order[256];
	unsigned char a[256];
	unsigned char b[256];
	unsigned char gx[256];
	unsigned char gy[256];

	unsigned char px[256];
	unsigned char py[256];
	unsigned char pz[256];
	unsigned char qx[256];
	unsigned char qy[256];
	unsigned char qz[256];
	unsigned char scalar[256];
	/* 15-points of each 3(X,Y,Z)-coordinates, and (9*8) bytes each co-ordinate */
	unsigned char fpm_table[4*1024]; //15*3*9*8]; 
};

struct nist_data {
	struct curve_data P192;
	struct curve_data P224;
	struct curve_data P256;
	struct curve_data P384;
	struct curve_data P521;
};
struct Brainpool_data {
	struct curve_data  P160;
	struct curve_data  P192;
	struct curve_data  P224;
	struct curve_data  P256;
	struct curve_data  P320;
	struct curve_data  P384;
	struct curve_data  P512;
};
struct secp_data {
	struct curve_data  P192;
	struct curve_data  P224;
	struct curve_data  P256;
};
struct FRP256v1_data {
	struct curve_data  P256;
};

struct prime_type {
	struct nist_data nist;
	struct Brainpool_data Brainpool;
	struct secp_data secp;
	struct FRP256v1_data FRP256v1;
};

struct ecc_data {
	struct prime_type prime;
};


void lookup_ECC_CurveParams(unsigned short int params, unsigned short int curves, struct curve_data *pCurveParams);
void n5_bignum_prep(unsigned char* str, int modlength, int z);
void n5_fill_context(unsigned char *x_coff, unsigned char *y_coff, unsigned char *prime, unsigned char *cptr, int prime_length, int affine_or_jacobian);
#endif
