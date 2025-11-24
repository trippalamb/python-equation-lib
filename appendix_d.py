"""
Appendix D: Equations Module

This module implements the equations defined in Appendix D of the TSEH5 specification.
Each function corresponds to a specific equation section and is designed to mirror
the mathematical notation as closely as possible for clarity.

Priority: Clarity with the document over computational efficiency.
"""

import math
from typing import Tuple, List

# Type aliases for clarity (matching document notation)
Vector3 = List[float]  # [x, y, z]
Matrix3x3 = List[List[float]]  # 3x3 matrix
Quaternion = List[float]  # [q_s, q_i, q_j, q_k]


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================
# These utility functions support the main equation implementations.
# They provide basic vector and matrix operations using only standard Python.

def vector_magnitude(v: Vector3) -> float:
    """
    Calculate the magnitude (norm) of a vector.

    ||v|| = sqrt(sum(v_i^2))

    Args:
        v: A 3-component vector [v_x, v_y, v_z]

    Returns:
        The Euclidean magnitude of the vector
    """
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)


def vector_normalize(v: Vector3) -> Vector3:
    """
    Normalize a vector to unit length.

    v_hat = v / ||v||

    Args:
        v: A 3-component vector [v_x, v_y, v_z]

    Returns:
        Unit vector in the same direction as v
    """
    mag = vector_magnitude(v)
    if mag == 0:
        return [0.0, 0.0, 0.0]
    return [v[0] / mag, v[1] / mag, v[2] / mag]


def vector_dot(a: Vector3, b: Vector3) -> float:
    """
    Calculate the dot product of two vectors.

    a . b = a_x*b_x + a_y*b_y + a_z*b_z

    Args:
        a: First 3-component vector
        b: Second 3-component vector

    Returns:
        Scalar dot product
    """
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]


def vector_cross(a: Vector3, b: Vector3) -> Vector3:
    """
    Calculate the cross product of two vectors.

    c = a x b

    Args:
        a: First 3-component vector
        b: Second 3-component vector

    Returns:
        Cross product vector
    """
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]


def vector_subtract(a: Vector3, b: Vector3) -> Vector3:
    """
    Subtract vector b from vector a.

    c = a - b

    Args:
        a: First 3-component vector
        b: Second 3-component vector

    Returns:
        Difference vector
    """
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def vector_add(a: Vector3, b: Vector3) -> Vector3:
    """
    Add two vectors.

    c = a + b

    Args:
        a: First 3-component vector
        b: Second 3-component vector

    Returns:
        Sum vector
    """
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]


def matrix_multiply(A: Matrix3x3, B: Matrix3x3) -> Matrix3x3:
    """
    Multiply two 3x3 matrices.

    C = A . B

    Args:
        A: First 3x3 matrix
        B: Second 3x3 matrix

    Returns:
        Product matrix C = A * B
    """
    C = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matrix_vector_multiply(M: Matrix3x3, v: Vector3) -> Vector3:
    """
    Multiply a 3x3 matrix by a 3-component vector.

    result = M . v

    Args:
        M: 3x3 matrix
        v: 3-component vector

    Returns:
        Resulting 3-component vector
    """
    return [
        M[0][0]*v[0] + M[0][1]*v[1] + M[0][2]*v[2],
        M[1][0]*v[0] + M[1][1]*v[1] + M[1][2]*v[2],
        M[2][0]*v[0] + M[2][1]*v[1] + M[2][2]*v[2]
    ]


def sign(x: float) -> float:
    """
    D.0.6.2 Sign Function

    sign(x) = { +1  if x > 0
              {  0  if x = 0
              { -1  if x < 0

    Args:
        x: Input value

    Returns:
        Sign of x (-1, 0, or +1)
    """
    if x > 0:
        return 1.0
    elif x < 0:
        return -1.0
    else:
        return 0.0


# =============================================================================
# D.1 ROTATIONAL STATE TRANSFORMATIONS
# =============================================================================

# -----------------------------------------------------------------------------
# D.1.1 DCM Rotations
# -----------------------------------------------------------------------------

def D_1_1_1_roll_rotation_matrix(phi: float) -> Matrix3x3:
    """
    D.1.1.1 Roll Rotation Matrix

    This matrix rotates vectors about the X-axis by angle phi, transforming
    coordinates in the YZ-plane while leaving the X-component unchanged.

    R_roll(phi) = | 1    0         0        |
                  | 0    cos(phi)  sin(phi) |
                  | 0   -sin(phi)  cos(phi) |

    Args:
        phi: Roll angle (rotation about X-axis) [radians]

    Returns:
        3x3 Roll Rotation Matrix
    """
    R_roll = [
        [1,            0,             0           ],
        [0,  math.cos(phi),  math.sin(phi)],
        [0, -math.sin(phi),  math.cos(phi)]
    ]
    return R_roll


def D_1_1_2_pitch_rotation_matrix(theta: float) -> Matrix3x3:
    """
    D.1.1.2 Pitch Rotation Matrix

    This matrix rotates vectors about the Y-axis by angle theta, transforming
    coordinates in the XZ-plane while leaving the Y-component unchanged.

    R_pitch(theta) = | cos(theta)  0  -sin(theta) |
                     |     0       1       0      |
                     | sin(theta)  0   cos(theta) |

    Args:
        theta: Pitch angle (rotation about Y-axis) [radians]

    Returns:
        3x3 Pitch Rotation Matrix
    """
    R_pitch = [
        [math.cos(theta), 0, -math.sin(theta)],
        [0,               1,  0              ],
        [math.sin(theta), 0,  math.cos(theta)]
    ]
    return R_pitch


def D_1_1_3_yaw_rotation_matrix(psi: float) -> Matrix3x3:
    """
    D.1.1.3 Yaw Rotation Matrix

    This matrix rotates vectors about the Z-axis by angle psi, transforming
    coordinates in the XY-plane while leaving the Z-component unchanged.

    R_yaw(psi) = |  cos(psi)  sin(psi)  0 |
                 | -sin(psi)  cos(psi)  0 |
                 |     0          0     1 |

    Args:
        psi: Yaw angle (rotation about Z-axis) [radians]

    Returns:
        3x3 Yaw Rotation Matrix
    """
    R_yaw = [
        [ math.cos(psi), math.sin(psi), 0],
        [-math.sin(psi), math.cos(psi), 0],
        [0,              0,             1]
    ]
    return R_yaw


def D_1_1_4_1_composite_dcm(phi: float, theta: float, psi: float) -> Matrix3x3:
    """
    D.1.1.4.1 Composite DCM (Yaw-Pitch-Roll Rotation Sequence)

    The full rotation matrix for a yaw-pitch-roll sequence is formed by
    multiplying the individual rotation matrices:

    DCM(phi, theta, psi) = R_roll(phi) . R_pitch(theta) . R_yaw(psi)

    Args:
        phi: Roll angle (rotation about X-axis) [radians]
        theta: Pitch angle (rotation about Y-axis) [radians]
        psi: Yaw angle (rotation about Z-axis) [radians]

    Returns:
        3x3 Direction Cosine Matrix for Yaw-Pitch-Roll rotation sequence
    """
    R_roll = D_1_1_1_roll_rotation_matrix(phi)
    R_pitch = D_1_1_2_pitch_rotation_matrix(theta)
    R_yaw = D_1_1_3_yaw_rotation_matrix(psi)

    # DCM = R_roll . R_pitch . R_yaw
    DCM = matrix_multiply(R_roll, matrix_multiply(R_pitch, R_yaw))
    return DCM


def D_1_1_4_2_expanded_dcm(phi: float, theta: float, psi: float) -> Matrix3x3:
    """
    D.1.1.4.2 Expanded Form DCM

    Expanding the matrix multiplication yields the following form in terms
    of all three Euler angles:

    DCM(phi, theta, psi) =
    | cos(theta)cos(psi)                              cos(theta)sin(psi)                             -sin(theta)           |
    | -cos(phi)sin(psi)+sin(phi)sin(theta)cos(psi)    cos(phi)cos(psi)+sin(phi)sin(theta)sin(psi)    sin(phi)cos(theta)    |
    | sin(phi)sin(psi)+cos(phi)sin(theta)cos(psi)    -sin(phi)cos(psi)+cos(phi)sin(theta)sin(psi)    cos(phi)cos(theta)    |

    Args:
        phi: Roll angle (rotation about X-axis) [radians]
        theta: Pitch angle (rotation about Y-axis) [radians]
        psi: Yaw angle (rotation about Z-axis) [radians]

    Returns:
        3x3 Direction Cosine Matrix (expanded form)
    """
    cos_phi = math.cos(phi)
    sin_phi = math.sin(phi)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    cos_psi = math.cos(psi)
    sin_psi = math.sin(psi)

    DCM = [
        [
            cos_theta * cos_psi,
            cos_theta * sin_psi,
            -sin_theta
        ],
        [
            -cos_phi * sin_psi + sin_phi * sin_theta * cos_psi,
            cos_phi * cos_psi + sin_phi * sin_theta * sin_psi,
            sin_phi * cos_theta
        ],
        [
            sin_phi * sin_psi + cos_phi * sin_theta * cos_psi,
            -sin_phi * cos_psi + cos_phi * sin_theta * sin_psi,
            cos_phi * cos_theta
        ]
    ]
    return DCM


# -----------------------------------------------------------------------------
# D.1.2 Quaternions and Euler Angles
# -----------------------------------------------------------------------------

def D_1_2_1_quaternion_to_euler(q_s: float, q_i: float, q_j: float, q_k: float) -> Tuple[float, float, float]:
    """
    D.1.2.1 Quaternion to Euler Angles

    These equations extract roll, pitch, and yaw Euler angles from quaternion components.

    phi   = arctan2(2(q_s*q_i + q_j*q_k), (q_s^2 - q_i^2 - q_j^2 + q_k^2))
    theta = arcsin(2(q_s*q_j - q_k*q_i))
    psi   = arctan2(2(q_s*q_k + q_i*q_j), (q_s^2 + q_i^2 - q_j^2 - q_k^2))

    Args:
        q_s: Scalar component (qs_i2b)
        q_i: i component (qi_i2b)
        q_j: j component (qj_i2b)
        q_k: k component (qk_i2b)

    Returns:
        Tuple of (phi, theta, psi) - roll, pitch, yaw angles [radians]
    """
    phi = math.atan2(
        2 * (q_s * q_i + q_j * q_k),
        (q_s**2 - q_i**2 - q_j**2 + q_k**2)
    )

    theta = math.asin(
        2 * (q_s * q_j - q_k * q_i)
    )

    psi = math.atan2(
        2 * (q_s * q_k + q_i * q_j),
        (q_s**2 + q_i**2 - q_j**2 - q_k**2)
    )

    return (phi, theta, psi)


def D_1_2_2_euler_to_quaternion(phi: float, theta: float, psi: float) -> Tuple[float, float, float, float]:
    """
    D.1.2.2 Euler Angles to Quaternion

    These equations convert roll, pitch, and yaw Euler angles into the four
    quaternion components.

    q_s = cos(psi/2)cos(theta/2)cos(phi/2) + sin(psi/2)sin(theta/2)sin(phi/2)
    q_i = cos(psi/2)cos(theta/2)sin(phi/2) - sin(psi/2)sin(theta/2)cos(phi/2)
    q_j = cos(psi/2)sin(theta/2)cos(phi/2) + sin(psi/2)cos(theta/2)sin(phi/2)
    q_k = sin(psi/2)cos(theta/2)cos(phi/2) - cos(psi/2)sin(theta/2)sin(phi/2)

    Args:
        phi: Roll angle [radians]
        theta: Pitch angle [radians]
        psi: Yaw angle [radians]

    Returns:
        Tuple of (q_s, q_i, q_j, q_k) - quaternion components
    """
    cos_psi_2 = math.cos(psi / 2)
    sin_psi_2 = math.sin(psi / 2)
    cos_theta_2 = math.cos(theta / 2)
    sin_theta_2 = math.sin(theta / 2)
    cos_phi_2 = math.cos(phi / 2)
    sin_phi_2 = math.sin(phi / 2)

    q_s = cos_psi_2 * cos_theta_2 * cos_phi_2 + sin_psi_2 * sin_theta_2 * sin_phi_2
    q_i = cos_psi_2 * cos_theta_2 * sin_phi_2 - sin_psi_2 * sin_theta_2 * cos_phi_2
    q_j = cos_psi_2 * sin_theta_2 * cos_phi_2 + sin_psi_2 * cos_theta_2 * sin_phi_2
    q_k = sin_psi_2 * cos_theta_2 * cos_phi_2 - cos_psi_2 * sin_theta_2 * sin_phi_2

    return (q_s, q_i, q_j, q_k)


def D_1_2_3_quaternion_to_body_direction(q_s: float, q_i: float, q_j: float, q_k: float) -> Vector3:
    """
    D.1.2.3 Quaternion to Body Direction Vector

    The x-body unit vector represents the missile's longitudinal axis direction
    in the reference frame. It corresponds to the first row of the rotation
    matrix derived from the quaternion.

    x_body = | 1 - 2(q_j^2 + q_k^2) |
             | 2(q_i*q_j + q_s*q_k) |
             | 2(q_i*q_k - q_s*q_j) |

    Args:
        q_s: Scalar component (qs_i2b)
        q_i: i component (qi_i2b)
        q_j: j component (qj_i2b)
        q_k: k component (qk_i2b)

    Returns:
        Body direction unit vector [x, y, z] in reference frame
    """
    x_body = [
        1 - 2 * (q_j**2 + q_k**2),
        2 * (q_i * q_j + q_s * q_k),
        2 * (q_i * q_k - q_s * q_j)
    ]
    return x_body


# =============================================================================
# D.2 SPATIAL STATE TRANSFORMATIONS
# =============================================================================
# Note: The appendix references coordinate transformations but D.2 section
# is not fully provided. We implement the referenced ECI to Body CG DCM
# which uses the Euler angles from the quaternion.

def D_2_1_2_1_eci_to_body_cg_dcm(phi: float, theta: float, psi: float) -> Matrix3x3:
    """
    D.2.1.2.1 ECI to Body CG DCM

    The DCM that transforms vectors from ECI frame to Body CG frame.
    Uses the yaw-pitch-roll rotation sequence.

    R_ECI_to_BodyCG = DCM(phi, theta, psi)

    Args:
        phi: Roll angle (I2B) [radians]
        theta: Pitch angle (I2B) [radians]
        psi: Yaw angle (I2B) [radians]

    Returns:
        3x3 DCM for ECI to Body CG transformation
    """
    return D_1_1_4_1_composite_dcm(phi, theta, psi)


# =============================================================================
# D.3 FLIGHT DATA
# =============================================================================

# -----------------------------------------------------------------------------
# D.3.1 Airspeed
# -----------------------------------------------------------------------------

def D_3_1_1_airspeed_eci(v_relative_eci: Vector3, v_wind_eci: Vector3) -> Vector3:
    """
    D.3.1.1 ECI Airspeed

    ECI airspeed represents the velocity of the object relative to the
    surrounding air mass, with vector components expressed in the inertial
    ECI frame.

    v_air_ECI = v_relative_ECI - v_wind_ECI

    Args:
        v_relative_eci: [m/s] Relative velocity vector in ECI frame
        v_wind_eci: [m/s] Wind velocity vector in ECI frame
                    [x_vel_eci_wind, y_vel_eci_wind, z_vel_eci_wind]

    Returns:
        [m/s] Airspeed vector in ECI frame
    """
    v_air_eci = vector_subtract(v_relative_eci, v_wind_eci)
    return v_air_eci


def D_3_1_2_airspeed_body_cg(R_eci_to_body_cg: Matrix3x3, v_air_eci: Vector3) -> Vector3:
    """
    D.3.1.2 Body CG Airspeed

    Body CG airspeed represents the airspeed vector rotated into the body-fixed
    reference frame with origin at the center of gravity.

    v_air_BodyCG = R_ECI_to_BodyCG . v_air_ECI

    Args:
        R_eci_to_body_cg: ECI to Body CG DCM (from D.2.1.2.1)
        v_air_eci: [m/s] Airspeed vector in ECI frame (from D.3.1.1)

    Returns:
        [m/s] Airspeed vector in Body CG frame
    """
    v_air_body_cg = matrix_vector_multiply(R_eci_to_body_cg, v_air_eci)
    return v_air_body_cg


# -----------------------------------------------------------------------------
# D.3.2 Angle of Attack
# -----------------------------------------------------------------------------

def D_3_2_1_total_angle_of_attack(v_air_body_cg: Vector3) -> float:
    """
    D.3.2.1 Total Angle of Attack

    The total angle of attack represents the angle between the body's
    longitudinal axis (x-axis) and the airspeed vector, regardless of
    the plane of rotation.

    aoa_total = { 0                                              if ||v_air_BodyCG|| = 0
                { arccos(v_x / ||v_air_BodyCG||)                 otherwise

    Args:
        v_air_body_cg: [m/s] Airspeed vector in Body CG frame (from D.3.1.2)

    Returns:
        [radians] Total angle of attack
    """
    v_magnitude = vector_magnitude(v_air_body_cg)

    if v_magnitude == 0:
        aoa_total = 0
    else:
        v_x = v_air_body_cg[0]
        aoa_total = math.acos(v_x / v_magnitude)

    return aoa_total


def D_3_2_2_pitch_angle_of_attack(v_air_body_cg: Vector3) -> float:
    """
    D.3.2.2 Pitch Angle of Attack

    The pitch angle of attack is the angle between the body x-axis and
    the projection of the airspeed vector onto the body x-z plane.

    aoa_alpha = arctan2(v_z, v_x)

    Args:
        v_air_body_cg: [m/s] Airspeed vector in Body CG frame (from D.3.1.2)

    Returns:
        [radians] Pitch angle of attack (alpha)
    """
    v_x = v_air_body_cg[0]
    v_z = v_air_body_cg[2]

    aoa_alpha = math.atan2(v_z, v_x)
    return aoa_alpha


def D_3_2_3_yaw_angle_of_attack(v_air_body_cg: Vector3) -> float:
    """
    D.3.2.3 Yaw Angle of Attack

    The yaw angle of attack (side slip angle) is the angle between the
    body x-axis and the projection of the airspeed vector onto the body
    x-y plane.

    aoa_beta = arctan2(v_y, v_x)

    Args:
        v_air_body_cg: [m/s] Airspeed vector in Body CG frame (from D.3.1.2)

    Returns:
        [radians] Yaw angle of attack (beta)
    """
    v_x = v_air_body_cg[0]
    v_y = v_air_body_cg[1]

    aoa_beta = math.atan2(v_y, v_x)
    return aoa_beta


# -----------------------------------------------------------------------------
# D.3.3 Flight Path Angle
# -----------------------------------------------------------------------------

def D_3_3_1_local_vertical_unit_vector(lat: float, lon: float) -> Vector3:
    """
    Helper function for D.3.3.1 and D.3.3.2

    The local vertical unit vector is calculated from geodetic coordinates:

    r_local = | cos(Lat) * cos(Lon) |
              | cos(Lat) * sin(Lon) |
              | sin(Lat)            |

    Args:
        lat: [radians] Geodetic latitude
        lon: [radians] Geodetic longitude

    Returns:
        Local vertical unit vector
    """
    r_local = [
        math.cos(lat) * math.cos(lon),
        math.cos(lat) * math.sin(lon),
        math.sin(lat)
    ]
    return r_local


def D_3_3_1_flight_path_angle_ecr(v_ecr: Vector3, lat: float, lon: float) -> float:
    """
    D.3.3.1 Flight Path Angle in ECR Frame

    The flight path angle in the ECR frame represents the angle relative
    to Earth's surface, as observed by ground-based observers.

    fpa_ECR = arcsin((v_ECR . r_local) / ||v_ECR||)

    Args:
        v_ecr: [m/s] Velocity vector in ECR frame
        lat: [radians] Geodetic latitude (from ECR to LLA)
        lon: [radians] Geodetic longitude (from ECR to LLA)

    Returns:
        [radians] Flight path angle in ECR frame (positive = climbing)
    """
    r_local = D_3_3_1_local_vertical_unit_vector(lat, lon)
    v_magnitude = vector_magnitude(v_ecr)

    if v_magnitude == 0:
        return 0.0

    fpa_ecr = math.asin(vector_dot(v_ecr, r_local) / v_magnitude)
    return fpa_ecr


def D_3_3_2_inertial_flight_path_angle(v_eci: Vector3, lat_eci: float, lon_eci: float) -> float:
    """
    D.3.3.2 Inertial Flight Path Angle

    The inertial flight path angle represents the flight path angle calculated
    in the inertial reference frame using ECI velocity.

    r_local_ECI = | cos(Lat_ECI) * cos(Lon_ECI) |
                  | cos(Lat_ECI) * sin(Lon_ECI) |
                  | sin(Lat_ECI)                |

    fpa_ECI = arcsin((v_ECI . r_local_ECI) / ||v_ECI||)

    Args:
        v_eci: [m/s] Velocity vector in ECI frame
        lat_eci: [radians] Geodetic latitude derived from ECI position using ECR to LLA
        lon_eci: [radians] Geodetic longitude derived from ECI position using ECR to LLA

    Returns:
        [radians] Inertial flight path angle
    """
    r_local_eci = D_3_3_1_local_vertical_unit_vector(lat_eci, lon_eci)
    v_magnitude = vector_magnitude(v_eci)

    if v_magnitude == 0:
        return 0.0

    fpa_eci = math.asin(vector_dot(v_eci, r_local_eci) / v_magnitude)
    return fpa_eci


# -----------------------------------------------------------------------------
# D.3.4 Precession and Spin
# -----------------------------------------------------------------------------

def D_3_4_1_lateral_angular_rate_magnitude(omega_q_body: float, omega_r_body: float) -> float:
    """
    D.3.4.1 Lateral Angular Rate Magnitude

    The lateral angular rate magnitude represents the combined magnitude of
    pitch and yaw angular rates.

    omega_s = sqrt(omega_q^2 + omega_r^2)

    Args:
        omega_q_body: [rad/s] Pitch rate of the body in Body CG frame (pit_rate)
        omega_r_body: [rad/s] Yaw rate of the body in Body CG frame (yaw_rate)

    Returns:
        [rad/s] Lateral angular rate magnitude
    """
    omega_s = math.sqrt(omega_q_body**2 + omega_r_body**2)
    return omega_s


def D_3_4_2_precession_angle(I_body_cg: Matrix3x3, omega_body: Vector3) -> float:
    """
    D.3.4.2 Precession Angle

    The precession angle represents the angle between the angular momentum
    vector and the body longitudinal axis (x-axis).

    H_BodyCG = I_BodyCG . omega_Body

    precession = { pi/2                                          if omega_p = 0
                 { arccos((H_BodyCG . omega_p) / ||H_BodyCG||)   otherwise

    Args:
        I_body_cg: [kg*m^2] Inertia tensor matrix in Body CG frame
        omega_body: [rad/s] Body rates [rol_rate, pit_rate, yaw_rate]

    Returns:
        [radians] Precession angle (coning half angle), range [0, pi/2]
    """
    omega_p_body = omega_body[0]  # Roll rate

    # H_BodyCG = I_BodyCG . omega_Body
    H_body_cg = matrix_vector_multiply(I_body_cg, omega_body)

    if omega_p_body == 0:
        precession = math.pi / 2
    else:
        H_magnitude = vector_magnitude(H_body_cg)
        if H_magnitude == 0:
            precession = math.pi / 2
        else:
            # The dot product with omega_p (scalar roll rate) seems to be intended
            # as projecting H onto the x-axis direction, so we use H[0] / ||H||
            precession = math.acos(H_body_cg[0] * omega_p_body / (H_magnitude * abs(omega_p_body)))

    return precession


def D_3_4_3_precession_rate(omega_s: float, precession: float, tolerance: float = 1e-10) -> float:
    """
    D.3.4.3 Precession Rate

    The precession rate represents the rate at which the body axis precesses
    about the angular momentum vector.

    precession_dot = { 0                            if precession ~ 0
                     { omega_s / sin(precession)    otherwise

    Args:
        omega_s: [rad/s] Lateral angular rate magnitude (from D.3.4.1)
        precession: [radians] Precession angle (from D.3.4.2)
        tolerance: Tolerance for checking if precession is approximately zero

    Returns:
        [rad/s] Precession rate (coning rate)
    """
    if abs(precession) < tolerance:
        precession_dot = 0
    else:
        precession_dot = omega_s / math.sin(precession)

    return precession_dot


def D_3_4_4_spin_angle(phi_spin_t0: float, roll_rate_integral: float) -> float:
    """
    D.3.4.4 Spin Angle

    The spin angle represents the cumulative angular rotation about the
    longitudinal body axis (x-axis) since trajectory initialization.

    phi_spin(t) = phi_spin(t_0) + integral(omega_p(tau), t_0, t)

    Then wrapped to [-pi, pi]:
    phi_spin = { phi_spin - 2*pi    if phi_spin > +pi
               { phi_spin + 2*pi    if phi_spin < -pi
               { phi_spin           otherwise

    Args:
        phi_spin_t0: [radians] Initial spin angle at t_0
        roll_rate_integral: [radians] Integral of roll rate from t_0 to t

    Returns:
        [radians] Spin angle at time t, range [-pi, pi]
    """
    phi_spin = phi_spin_t0 + roll_rate_integral

    # Wrap to [-pi, pi]
    while phi_spin > math.pi:
        phi_spin = phi_spin - 2 * math.pi
    while phi_spin < -math.pi:
        phi_spin = phi_spin + 2 * math.pi

    return phi_spin


def D_3_4_5_spin_rate(omega_p_body: float) -> float:
    """
    D.3.4.5 Spin Rate

    The spin rate represents the rate of change of the spin angle about
    the longitudinal body axis. Spin rate equals the roll rate.

    phi_spin_dot = omega_p

    Args:
        omega_p_body: [rad/s] Roll rate of the body in Body CG frame (rol_rate)

    Returns:
        [rad/s] Spin rate
    """
    phi_spin_dot = omega_p_body
    return phi_spin_dot


# -----------------------------------------------------------------------------
# D.3.5 Mach Number
# -----------------------------------------------------------------------------

# Constants for Mach number calculation
GAMMA_AIR = 1.4  # Specific heat ratio for air (dimensionless)
R_AIR = 287.052874247  # Specific gas constant for air [J/(kg*K)]


def D_3_5_speed_of_sound(T_atmos: float) -> float:
    """
    Helper function for D.3.5 Mach Number

    v_sound = sqrt(gamma_air * R_air * T_atmos)

    Args:
        T_atmos: [K] Atmospheric temperature (temperature_atmospheric)

    Returns:
        [m/s] Speed of sound in air
    """
    v_sound = math.sqrt(GAMMA_AIR * R_AIR * T_atmos)
    return v_sound


def D_3_5_mach_number(v_air_eci: Vector3, T_atmos: float) -> float:
    """
    D.3.5 Mach Number

    The Mach number represents the ratio of airspeed to the local speed of sound.

    v_sound = sqrt(gamma_air * R_air * T_atmos)
    mach = ||v_air_ECI|| / v_sound

    Args:
        v_air_eci: [m/s] Airspeed vector in ECI frame (from D.3.1.1)
        T_atmos: [K] Atmospheric temperature (temperature_atmospheric)

    Returns:
        Mach number (dimensionless)
    """
    v_sound = D_3_5_speed_of_sound(T_atmos)
    v_air_magnitude = vector_magnitude(v_air_eci)

    mach = v_air_magnitude / v_sound
    return mach


# -----------------------------------------------------------------------------
# D.3.6 Sensed Acceleration
# -----------------------------------------------------------------------------

def D_3_6_1_sensed_acceleration_eci(a_eci: Vector3, a_gravity_eci: Vector3) -> Vector3:
    """
    D.3.6.1 ECI Sensed Acceleration

    The sensed acceleration calculation begins in the ECI frame by removing
    gravitational acceleration from the total acceleration.

    a_sensed_ECI = a_ECI - a_gravity_ECI

    Args:
        a_eci: [m/s^2] Acceleration vector in ECI frame
               [x_acc_eci, y_acc_eci, z_acc_eci]
        a_gravity_eci: [m/s^2] Gravitational acceleration vector in ECI frame
                       [x_acc_eci_gravity, y_acc_eci_gravity, z_acc_eci_gravity]

    Returns:
        [m/s^2] Sensed acceleration vector in ECI frame
    """
    a_sensed_eci = vector_subtract(a_eci, a_gravity_eci)
    return a_sensed_eci


def D_3_6_2_sensed_acceleration_body_cg(R_eci_to_body_cg: Matrix3x3, a_sensed_eci: Vector3) -> Vector3:
    """
    D.3.6.2 Body CG Sensed Acceleration

    The sensed acceleration vector is then transformed from the ECI frame
    to the Body CG frame using the rotation matrix.

    a_sensed_BodyCG = R_ECI_to_BodyCG . a_sensed_ECI

    Args:
        R_eci_to_body_cg: ECI to Body CG DCM (from D.2.1.2.1)
        a_sensed_eci: [m/s^2] Sensed acceleration vector in ECI frame (from D.3.6.1)

    Returns:
        [m/s^2] Sensed acceleration vector in Body CG frame
                [a_x_sensed, a_y_sensed, a_z_sensed]
    """
    a_sensed_body_cg = matrix_vector_multiply(R_eci_to_body_cg, a_sensed_eci)
    return a_sensed_body_cg


def D_3_6_3_lateral_sensed_acceleration(a_sensed_body_cg: Vector3) -> float:
    """
    D.3.6.3 Lateral Sensed Acceleration

    The lateral sensed acceleration represents the magnitude of sensed
    acceleration perpendicular to the body longitudinal axis.

    a_lateral_sensed = sqrt(a_y_sensed^2 + a_z_sensed^2)

    Args:
        a_sensed_body_cg: [m/s^2] Sensed acceleration in Body CG frame (from D.3.6.2)

    Returns:
        [m/s^2] Lateral sensed acceleration magnitude
    """
    a_y_sensed = a_sensed_body_cg[1]
    a_z_sensed = a_sensed_body_cg[2]

    a_lateral_sensed = math.sqrt(a_y_sensed**2 + a_z_sensed**2)
    return a_lateral_sensed


# =============================================================================
# D.4 AERODYNAMIC COEFFICIENTS
# =============================================================================

def D_4_1_dynamic_pressure(rho_atmos: float, v_air_body_cg: Vector3) -> float:
    """
    D.4.1 Dynamic Pressure

    Dynamic pressure represents the kinetic energy per unit volume of the
    airflow around the object.

    P_dynamic = (1/2) * rho_atmos * ||v_air_BodyCG||^2

    Args:
        rho_atmos: [kg/m^3] Atmospheric density (density_atmospheric)
        v_air_body_cg: [m/s] Airspeed vector in body frame (from D.3.1.2)

    Returns:
        [Pa] Dynamic pressure
    """
    v_magnitude = vector_magnitude(v_air_body_cg)
    P_dynamic = (1/2) * rho_atmos * v_magnitude**2
    return P_dynamic


def D_4_2_reference_area(m: float, C_ballistic: float, C_D: float) -> float:
    """
    D.4.2 Reference Area

    The reference area is a characteristic area used to non-dimensionalize
    aerodynamic forces.

    S_ref = m / (C_Ballistic * C_D)

    Args:
        m: [kg] Object mass (mass)
        C_ballistic: [kg/m^2] Ballistic coefficient (coefficient_ballistic)
        C_D: Drag coefficient (coefficient_drag)

    Returns:
        [m^2] Aerodynamic reference area
    """
    S_ref = m / (C_ballistic * C_D)
    return S_ref


def D_4_3_axial_force_coefficient(F_x_aero: float, P_dynamic: float, S_ref: float) -> float:
    """
    D.4.3 Axial Force Coefficient

    The axial force coefficient represents the component of aerodynamic force
    along the body longitudinal axis (x-axis), normalized by dynamic pressure
    and reference area.

    C_a = F_x_aero / (P_dynamic * S_ref)

    Args:
        F_x_aero: [N] Aerodynamic force along body x-axis (x_force_aero)
        P_dynamic: [Pa] Dynamic pressure (from D.4.1)
        S_ref: [m^2] Reference area (from D.4.2)

    Returns:
        Axial force coefficient (dimensionless)
    """
    if P_dynamic * S_ref == 0:
        return 0.0
    C_a = F_x_aero / (P_dynamic * S_ref)
    return C_a


def D_4_4_normal_force_coefficient(F_z_aero: float, P_dynamic: float, S_ref: float) -> float:
    """
    D.4.4 Normal Force Coefficient

    The normal force coefficient represents the component of aerodynamic force
    along the body ventral axis (z-axis), normalized by dynamic pressure and
    reference area.

    C_n = F_z_aero / (P_dynamic * S_ref)

    Args:
        F_z_aero: [N] Aerodynamic force along body z-axis (z_force_aero)
        P_dynamic: [Pa] Dynamic pressure (from D.4.1)
        S_ref: [m^2] Reference area (from D.4.2)

    Returns:
        Normal force coefficient (dimensionless)
    """
    if P_dynamic * S_ref == 0:
        return 0.0
    C_n = F_z_aero / (P_dynamic * S_ref)
    return C_n


def D_4_5_lift_coefficient(aoa_alpha: float, C_a: float, C_n: float) -> float:
    """
    D.4.5 Lift Coefficient

    The lift coefficient represents the aerodynamic force component perpendicular
    to the airspeed direction, normalized by dynamic pressure and reference area.

    C_L = -sin(aoa_alpha) * C_a + cos(aoa_alpha) * C_n

    Args:
        aoa_alpha: [radians] Pitch angle of attack (from D.3.2.2)
        C_a: Axial force coefficient (from D.4.3)
        C_n: Normal force coefficient (from D.4.4)

    Returns:
        Lift coefficient (dimensionless)
    """
    C_L = -math.sin(aoa_alpha) * C_a + math.cos(aoa_alpha) * C_n
    return C_L


# =============================================================================
# D.5 MASS PROPERTIES
# =============================================================================

def D_5_1_1_inertia_tensor(I_xx: float, I_yy: float, I_zz: float,
                           I_xy: float, I_xz: float, I_yz: float) -> Matrix3x3:
    """
    D.5.1.1 Inertia Tensor Matrix Form

    The inertia tensor is a symmetric 3x3 matrix that characterizes the mass
    distribution of the object relative to the Body CG coordinate frame.

    I_BodyCG = | I_xx  I_xy  I_xz |
               | I_yx  I_yy  I_yz |
               | I_zx  I_zy  I_zz |

    Where I_xy = I_yx, I_xz = I_zx, I_yz = I_zy (symmetric)

    Args:
        I_xx: [kg*m^2] Moment of inertia about x-axis (xx_moment_inertia)
        I_yy: [kg*m^2] Moment of inertia about y-axis (yy_moment_inertia)
        I_zz: [kg*m^2] Moment of inertia about z-axis (zz_moment_inertia)
        I_xy: [kg*m^2] Product of inertia for x-y plane (xy_product_inertia)
        I_xz: [kg*m^2] Product of inertia for x-z plane (xz_product_inertia)
        I_yz: [kg*m^2] Product of inertia for y-z plane (yz_product_inertia)

    Returns:
        3x3 Inertia tensor matrix in Body CG frame
    """
    I_body_cg = [
        [I_xx, I_xy, I_xz],
        [I_xy, I_yy, I_yz],
        [I_xz, I_yz, I_zz]
    ]
    return I_body_cg


# Note: D.5.1.2 and D.5.1.3 are integral definitions describing how moments
# and products of inertia are computed from mass distributions. They are not
# implemented as functions since they require volume integration over the
# object geometry, which is typically done by CAD software or lookup tables.


# =============================================================================
# D.6 PROPULSION
# =============================================================================

def D_6_1_thrust_magnitude(F_x_propulsion: float, F_y_propulsion: float,
                           F_z_propulsion: float) -> float:
    """
    D.6.1 Thrust Relationship

    The thrust magnitude represents the total propulsion force applied to the
    vehicle, calculated from the vector magnitude of the three body-axis force
    components.

    F_propulsion = [F_x, F_y, F_z]
    Thrust = ||F_propulsion|| = sqrt(F_x^2 + F_y^2 + F_z^2)

    Args:
        F_x_propulsion: [N] Propulsion force along body x-axis (x_force_propulsion)
        F_y_propulsion: [N] Propulsion force along body y-axis (y_force_propulsion)
        F_z_propulsion: [N] Propulsion force along body z-axis (z_force_propulsion)

    Returns:
        [N] Magnitude of the total propulsion force
    """
    F_propulsion = [F_x_propulsion, F_y_propulsion, F_z_propulsion]
    Thrust = vector_magnitude(F_propulsion)
    return Thrust


# =============================================================================
# D.7 GEODESY
# =============================================================================

def D_7_1_1_vincenty_ground_range(lat1: float, lon1: float,
                                   lat2: float, lon2: float,
                                   a: float = 6378137.0,
                                   f: float = 1/298.257223563,
                                   max_iterations: int = 200,
                                   tolerance: float = 1e-12) -> float:
    """
    D.7.1.1 Point-to-Point Ground Range (Vincenty's Formula)

    Vincenty's formula calculates the geodesic distance between any two
    geodetic positions (latitude, longitude). This represents the shortest
    path along the ellipsoid surface between those points.

    Reference: Vincenty, T. (1975). Direct and Inverse Solutions of Geodesics
    on the Ellipsoid with Application of Nested Equations.

    Args:
        lat1: [radians] Geodetic latitude of first point
        lon1: [radians] Geodetic longitude of first point
        lat2: [radians] Geodetic latitude of second point
        lon2: [radians] Geodetic longitude of second point
        a: [meters] Semi-major axis of ellipsoid (default: WGS84)
        f: Flattening of ellipsoid (default: WGS84)
        max_iterations: Maximum iterations for convergence
        tolerance: Convergence tolerance

    Returns:
        [meters] Geodesic distance between the two points
    """
    # Handle coincident points
    if lat1 == lat2 and lon1 == lon2:
        return 0.0

    # Semi-minor axis
    b = a * (1 - f)

    # Reduced latitudes
    U1 = math.atan((1 - f) * math.tan(lat1))
    U2 = math.atan((1 - f) * math.tan(lat2))

    sin_U1 = math.sin(U1)
    cos_U1 = math.cos(U1)
    sin_U2 = math.sin(U2)
    cos_U2 = math.cos(U2)

    # Difference in longitude
    L = lon2 - lon1
    lambda_prev = L

    for iteration in range(max_iterations):
        sin_lambda = math.sin(lambda_prev)
        cos_lambda = math.cos(lambda_prev)

        sin_sigma = math.sqrt(
            (cos_U2 * sin_lambda)**2 +
            (cos_U1 * sin_U2 - sin_U1 * cos_U2 * cos_lambda)**2
        )

        if sin_sigma == 0:
            return 0.0  # Coincident points

        cos_sigma = sin_U1 * sin_U2 + cos_U1 * cos_U2 * cos_lambda
        sigma = math.atan2(sin_sigma, cos_sigma)

        sin_alpha = cos_U1 * cos_U2 * sin_lambda / sin_sigma
        cos_sq_alpha = 1 - sin_alpha**2

        if cos_sq_alpha == 0:
            cos_2sigma_m = 0
        else:
            cos_2sigma_m = cos_sigma - 2 * sin_U1 * sin_U2 / cos_sq_alpha

        C = f / 16 * cos_sq_alpha * (4 + f * (4 - 3 * cos_sq_alpha))

        lambda_new = L + (1 - C) * f * sin_alpha * (
            sigma + C * sin_sigma * (
                cos_2sigma_m + C * cos_sigma * (-1 + 2 * cos_2sigma_m**2)
            )
        )

        if abs(lambda_new - lambda_prev) < tolerance:
            break

        lambda_prev = lambda_new

    # Calculate distance
    u_sq = cos_sq_alpha * (a**2 - b**2) / b**2
    A = 1 + u_sq / 16384 * (4096 + u_sq * (-768 + u_sq * (320 - 175 * u_sq)))
    B = u_sq / 1024 * (256 + u_sq * (-128 + u_sq * (74 - 47 * u_sq)))

    delta_sigma = B * sin_sigma * (
        cos_2sigma_m + B / 4 * (
            cos_sigma * (-1 + 2 * cos_2sigma_m**2) -
            B / 6 * cos_2sigma_m * (-3 + 4 * sin_sigma**2) * (-3 + 4 * cos_2sigma_m**2)
        )
    )

    s = b * A * (sigma - delta_sigma)

    return s


def D_7_1_2_ground_range_traveled(lla_points: List[Tuple[float, float, float]],
                                   a: float = 6378137.0,
                                   f: float = 1/298.257223563) -> float:
    """
    D.7.1.2 Ground Range Traveled

    The cumulative ground range traveled along a trajectory requires numerical
    integration. At each timestep, calculate the ground range between consecutive
    trajectory positions using Vincenty's formula, then sum these incremental
    distances.

    Ground_Range_Traveled(t_n) = sum(Ground_Range(LLA_{i-1}, LLA_i), i=1 to n)

    Args:
        lla_points: List of (latitude, longitude, altitude) tuples in radians/meters
                    representing trajectory positions
        a: [meters] Semi-major axis of ellipsoid (default: WGS84)
        f: Flattening of ellipsoid (default: WGS84)

    Returns:
        [meters] Total ground range traveled along the trajectory
    """
    if len(lla_points) < 2:
        return 0.0

    ground_range_traveled = 0.0

    for i in range(1, len(lla_points)):
        lat1, lon1, alt1 = lla_points[i - 1]
        lat2, lon2, alt2 = lla_points[i]

        ground_range = D_7_1_1_vincenty_ground_range(lat1, lon1, lat2, lon2, a, f)
        ground_range_traveled = ground_range_traveled + ground_range

    return ground_range_traveled


def D_7_2_prime_vertical_radius(r_a: float, epsilon_sq: float, lat: float) -> float:
    """
    D.7.2 Prime Vertical Radius

    The prime vertical radius represents the radius of curvature in the plane
    perpendicular to the meridian at a given geodetic latitude.

    r_pv = r_a / sqrt(1 - epsilon^2 * sin^2(Lat))

    Args:
        r_a: [meters] Earth semi-major axis (from Earth model)
        epsilon_sq: First eccentricity squared (from Earth model)
        lat: [radians] Geodetic latitude

    Returns:
        [meters] Prime vertical radius at reference latitude
    """
    r_pv = r_a / math.sqrt(1 - epsilon_sq * math.sin(lat)**2)
    return r_pv


def D_7_3_geoid_correction_term(epsilon_sq: float, r_pv: float, lat: float) -> float:
    """
    D.7.3 Geoid Correction Term

    The geoid correction term accounts for the difference between the geocentric
    and geodetic vertical references due to Earth's ellipsoidal shape.

    z_geoid = epsilon^2 * r_pv * sin(Lat)

    Args:
        epsilon_sq: First eccentricity squared (from Earth model)
        r_pv: [meters] Prime vertical radius (from D.7.2)
        lat: [radians] Geodetic latitude

    Returns:
        [meters] Geoid correction term
    """
    z_geoid = epsilon_sq * r_pv * math.sin(lat)
    return z_geoid


# =============================================================================
# D.8 BASIC UNIT CONVERSIONS
# =============================================================================

def D_8_1_radians_to_degrees(theta_radians: float) -> float:
    """
    D.8.1 Radians to Degrees

    Angle conversion from radians to degrees.

    theta_degrees = theta_radians * (180 / pi)

    Args:
        theta_radians: [radians] Angle value

    Returns:
        [degrees] Angle value
    """
    theta_degrees = theta_radians * (180 / math.pi)
    return theta_degrees


def D_8_2_degrees_to_radians(theta_degrees: float) -> float:
    """
    D.8.2 Degrees to Radians

    Angle conversion from degrees to radians.

    theta_radians = theta_degrees * (pi / 180)

    Args:
        theta_degrees: [degrees] Angle value

    Returns:
        [radians] Angle value
    """
    theta_radians = theta_degrees * (math.pi / 180)
    return theta_radians


def D_8_3_meters_to_kilometers(d_meters: float) -> float:
    """
    D.8.3 Meters to Kilometers

    Distance conversion from meters to kilometers.

    d_kilometers = d_meters / 1000

    Args:
        d_meters: [meters] Distance

    Returns:
        [kilometers] Distance
    """
    d_kilometers = d_meters / 1000
    return d_kilometers


# =============================================================================
# MODULE INFORMATION
# =============================================================================

__all__ = [
    # Utility functions
    'vector_magnitude',
    'vector_normalize',
    'vector_dot',
    'vector_cross',
    'vector_subtract',
    'vector_add',
    'matrix_multiply',
    'matrix_vector_multiply',
    'sign',

    # D.1 Rotational State Transformations
    'D_1_1_1_roll_rotation_matrix',
    'D_1_1_2_pitch_rotation_matrix',
    'D_1_1_3_yaw_rotation_matrix',
    'D_1_1_4_1_composite_dcm',
    'D_1_1_4_2_expanded_dcm',
    'D_1_2_1_quaternion_to_euler',
    'D_1_2_2_euler_to_quaternion',
    'D_1_2_3_quaternion_to_body_direction',

    # D.2 Spatial State Transformations
    'D_2_1_2_1_eci_to_body_cg_dcm',

    # D.3 Flight Data
    'D_3_1_1_airspeed_eci',
    'D_3_1_2_airspeed_body_cg',
    'D_3_2_1_total_angle_of_attack',
    'D_3_2_2_pitch_angle_of_attack',
    'D_3_2_3_yaw_angle_of_attack',
    'D_3_3_1_local_vertical_unit_vector',
    'D_3_3_1_flight_path_angle_ecr',
    'D_3_3_2_inertial_flight_path_angle',
    'D_3_4_1_lateral_angular_rate_magnitude',
    'D_3_4_2_precession_angle',
    'D_3_4_3_precession_rate',
    'D_3_4_4_spin_angle',
    'D_3_4_5_spin_rate',
    'D_3_5_speed_of_sound',
    'D_3_5_mach_number',
    'D_3_6_1_sensed_acceleration_eci',
    'D_3_6_2_sensed_acceleration_body_cg',
    'D_3_6_3_lateral_sensed_acceleration',

    # D.4 Aerodynamic Coefficients
    'D_4_1_dynamic_pressure',
    'D_4_2_reference_area',
    'D_4_3_axial_force_coefficient',
    'D_4_4_normal_force_coefficient',
    'D_4_5_lift_coefficient',

    # D.5 Mass Properties
    'D_5_1_1_inertia_tensor',

    # D.6 Propulsion
    'D_6_1_thrust_magnitude',

    # D.7 Geodesy
    'D_7_1_1_vincenty_ground_range',
    'D_7_1_2_ground_range_traveled',
    'D_7_2_prime_vertical_radius',
    'D_7_3_geoid_correction_term',

    # D.8 Unit Conversions
    'D_8_1_radians_to_degrees',
    'D_8_2_degrees_to_radians',
    'D_8_3_meters_to_kilometers',

    # Constants
    'GAMMA_AIR',
    'R_AIR',
]
